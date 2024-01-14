Configuration
#############

| Configuration files for *gallery-dl* use a JSON-based file format.
| For a (more or less) complete example with options set to their default values,
  see `gallery-dl.conf <gallery-dl.conf>`__.
| For a configuration file example with more involved settings and options,
  see `gallery-dl-example.conf <gallery-dl-example.conf>`__.
|

This file lists all available configuration options and their descriptions.


Contents
========

1) `Extractor Options`_
2) `Extractor-specific Options`_
3) `Downloader Options`_
4) `Output Options`_
5) `Postprocessor Options`_
6) `Miscellaneous Options`_
7) `API Tokens & IDs`_


Extractor Options
=================


Each extractor is identified by its ``category`` and ``subcategory``.
The ``category`` is the lowercase site name without any spaces or special
characters, which is usually just the module name
(``pixiv``, ``danbooru``, ...).
The ``subcategory`` is a lowercase word describing the general functionality
of that extractor (``user``, ``favorite``, ``manga``, ...).

Each one of the following options can be specified on multiple levels of the
configuration tree:

================== =======
Base level:        ``extractor.<option-name>``
Category level:    ``extractor.<category>.<option-name>``
Subcategory level: ``extractor.<category>.<subcategory>.<option-name>``
================== =======

A value in a "deeper" level hereby overrides a value of the same name on a
lower level. Setting the ``extractor.pixiv.filename`` value, for example, lets
you specify a general filename pattern for all the different pixiv extractors.
Using the ``extractor.pixiv.user.filename`` value lets you override this
general pattern specifically for ``PixivUserExtractor`` instances.

The ``category`` and ``subcategory`` of all extractors are included in the
output of ``gallery-dl --list-extractors``. For a specific URL these values
can also be determined by using the ``-K``/``--list-keywords`` command-line
option (see the example below).


extractor.*.filename
--------------------
Type
    * ``string``
    * ``object`` (`condition` -> `format string`_)
Example
    .. code:: json

        "{manga}_c{chapter}_{page:>03}.{extension}"

    .. code:: json

        {
            "extension == 'mp4'": "{id}_video.{extension}",
            "'nature' in title" : "{id}_{title}.{extension}",
            ""                  : "{id}_default.{extension}"
        }

Description
    A `format string`_ to build filenames for downloaded files with.

    If this is an ``object``, it must contain Python expressions mapping to the
    filename format strings to use.
    These expressions are evaluated in the order as specified in Python 3.6+
    and in an undetermined order in Python 3.4 and 3.5.

    The available replacement keys depend on the extractor used. A list
    of keys for a specific one can be acquired by calling *gallery-dl*
    with the ``-K``/``--list-keywords`` command-line option.
    For example:

    .. code::

        $ gallery-dl -K http://seiga.nicovideo.jp/seiga/im5977527
        Keywords for directory names:
        -----------------------------
        category
          seiga
        subcategory
          image

        Keywords for filenames:
        -----------------------
        category
          seiga
        extension
          None
        image-id
          5977527
        subcategory
          image

    Note: Even if the value of the ``extension`` key is missing or
    ``None``, it will be filled in later when the file download is
    starting. This key is therefore always available to provide
    a valid filename extension.


extractor.*.directory
---------------------
Type
    * ``list`` of ``strings``
    * ``object`` (`condition` -> `format strings`_)
Example
    .. code:: json

        ["{category}", "{manga}", "c{chapter} - {title}"]

    .. code:: json

        {
            "'nature' in content": ["Nature Pictures"],
            "retweet_id != 0"    : ["{category}", "{user[name]}", "Retweets"],
            ""                   : ["{category}", "{user[name]}"]
        }

Description
    A list of `format strings`_ to build target directory paths with.

    If this is an ``object``, it must contain Python expressions mapping to the
    list of format strings to use.

    Each individual string in such a list represents a single path
    segment, which will be joined together and appended to the
    base-directory_ to form the complete target directory path.


extractor.*.base-directory
--------------------------
Type
    |Path|_
Default
    ``"./gallery-dl/"``
Description
    Directory path used as base for all download destinations.


extractor.*.parent-directory
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Use an extractor's current target directory as
    `base-directory <extractor.*.base-directory_>`__
    for any spawned child extractors.


extractor.*.parent-metadata
---------------------------
extractor.*.metadata-parent
---------------------------
Type
    * ``bool``
    * ``string``
Default
    ``false``
Description
    If ``true``, overwrite any metadata provided by a child extractor
    with its parent's.

    | If this is a ``string``, add a parent's metadata to its children's
      to a field named after said string.
    | For example with ``"parent-metadata": "_p_"``:

    .. code:: json

        {
            "id": "child-id",
            "_p_": {"id": "parent-id"}
        }


extractor.*.parent-skip
-----------------------
Type
    ``bool``
Default
    ``false``
Description
    Share number of skipped downloads between parent and child extractors.


extractor.*.path-restrict
-------------------------
Type
    * ``string``
    * ``object`` (`character` -> `replacement character(s)`)
Default
    ``"auto"``
Example
    * ``"/!? (){}"``
    * ``{" ": "_", "/": "-", "|": "-", ":": "_-_", "*": "_+_"}``
Description
    | A string of characters to be replaced with the value of
      `path-replace <extractor.*.path-replace_>`__
    | or an object mapping invalid/unwanted characters to their replacements
    | for generated path segment names.

    Special values:

    * ``"auto"``: Use characters from ``"unix"`` or ``"windows"``
      depending on the local operating system
    * ``"unix"``: ``"/"``
    * ``"windows"``: ``"\\\\|/<>:\"?*"``
    * ``"ascii"``: ``"^0-9A-Za-z_."`` (only ASCII digits, letters, underscores, and dots)
    * ``"ascii+"``: ``"^0-9@-[\\]-{ #-)+-.;=!}~"`` (all ASCII characters except the ones not allowed by Windows)

    Implementation Detail: For ``strings`` with length >= 2, this option uses a
    `Regular Expression Character Set <https://www.regular-expressions.info/charclass.html>`__,
    meaning that:

    * using a caret ``^`` as first character inverts the set
    * character ranges are supported (``0-9a-z``)
    * ``]``, ``-``, and ``\`` need to be escaped as
      ``\\]``, ``\\-``, and ``\\\\`` respectively
      to use them as literal characters


extractor.*.path-replace
------------------------
Type
    ``string``
Default
    ``"_"``
Description
    The replacement character(s) for
    `path-restrict <extractor.*.path-restrict_>`__


extractor.*.path-remove
-----------------------
Type
    ``string``
Default
    ``"\u0000-\u001f\u007f"`` (ASCII control characters)
Description
    Set of characters to remove from generated path names.

    Note: In a string with 2 or more characters, ``[]^-\`` need to be
    escaped with backslashes, e.g. ``"\\[\\]"``


extractor.*.path-strip
----------------------
Type
    ``string``
Default
    ``"auto"``
Description
    Set of characters to remove from the end of generated path segment names
    using `str.rstrip() <https://docs.python.org/3/library/stdtypes.html#str.rstrip>`_

    Special values:

    * ``"auto"``: Use characters from ``"unix"`` or ``"windows"``
      depending on the local operating system
    * ``"unix"``: ``""``
    * ``"windows"``: ``". "``


extractor.*.path-extended
-------------------------
Type
    ``bool``
Default
    ``true``
Description
    On Windows, use `extended-length paths <https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation>`__
    prefixed with ``\\?\`` to work around the 260 characters path length limit.


extractor.*.extension-map
-------------------------
Type
    ``object`` (`extension` -> `replacement`)
Default
    .. code:: json

        {
            "jpeg": "jpg",
            "jpe" : "jpg",
            "jfif": "jpg",
            "jif" : "jpg",
            "jfi" : "jpg"
        }
Description
    A JSON ``object`` mapping filename extensions to their replacements.


extractor.*.skip
----------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Controls the behavior when downloading files that have been
    downloaded before, i.e. a file with the same filename already
    exists or its ID is in a `download archive <extractor.*.archive_>`__.

    * ``true``: Skip downloads
    * ``false``: Overwrite already existing files

    * ``"abort"``: Stop the current extractor run
    * ``"abort:N"``: Skip downloads and stop the current extractor run
      after ``N`` consecutive skips

    * ``"terminate"``: Stop the current extractor run, including parent extractors
    * ``"terminate:N"``: Skip downloads and stop the current extractor run,
      including parent extractors, after ``N`` consecutive skips

    * ``"exit"``: Exit the program altogether
    * ``"exit:N"``: Skip downloads and exit the program
      after ``N`` consecutive skips

    * ``"enumerate"``: Add an enumeration index to the beginning of the
      filename extension (``file.1.ext``, ``file.2.ext``, etc.)


extractor.*.sleep
-----------------
Type
    |Duration|_
Default
    ``0``
Description
    Number of seconds to sleep before each download.


extractor.*.sleep-extractor
---------------------------
Type
    |Duration|_
Default
    ``0``
Description
    Number of seconds to sleep before handling an input URL,
    i.e. before starting a new extractor.


extractor.*.sleep-request
-------------------------
Type
    |Duration|_
Default
    ``0``
Description
    Minimal time interval in seconds between each HTTP request
    during data extraction.


extractor.*.username & .password
--------------------------------
Type
    ``string``
Default
    ``null``
Description
    The username and password to use when attempting to log in to
    another site.

    Specifying username and password is required for

    * ``nijie``

    and optional for

    * ``aibooru`` (*)
    * ``aryion``
    * ``atfbooru`` (*)
    * ``danbooru`` (*)
    * ``e621`` (*)
    * ``e926`` (*)
    * ``exhentai``
    * ``idolcomplex``
    * ``imgbb``
    * ``inkbunny``
    * ``kemonoparty``
    * ``mangadex``
    * ``mangoxo``
    * ``pillowfort``
    * ``sankaku``
    * ``seisoparty``
    * ``subscribestar``
    * ``tapas``
    * ``tsumino``
    * ``twitter``
    * ``vipergirls``
    * ``zerochan``

    These values can also be specified via the
    ``-u/--username`` and ``-p/--password`` command-line options or
    by using a |.netrc|_ file. (see Authentication_)

    (*) The password value for these sites should be
    the API key found in your user profile, not the actual account password.

    Note: Leave the ``password`` value empty or undefined
    to get prompted for a passeword when performing a login
    (see `getpass() <https://docs.python.org/3/library/getpass.html#getpass.getpass>`__).


extractor.*.netrc
-----------------
Type
    ``bool``
Default
    ``false``
Description
    Enable the use of |.netrc|_ authentication data.


extractor.*.cookies
-------------------
Type
    * |Path|_
    * ``object`` (`name` -> `value`)
    * ``list``
Description
    Source to read additional cookies from. This can be

    * The |Path|_ to a Mozilla/Netscape format cookies.txt file

      .. code:: json

        "~/.local/share/cookies-instagram-com.txt"

    * An ``object`` specifying cookies as name-value pairs

      .. code:: json

        {
            "cookie-name": "cookie-value",
            "sessionid"  : "14313336321%3AsabDFvuASDnlpb%3A31",
            "isAdult"    : "1"
        }

    * A ``list`` with up to 5 entries specifying a browser profile.

      * The first entry is the browser name
      * The optional second entry is a profile name or an absolute path to a profile directory
      * The optional third entry is the keyring to retrieve passwords for decrypting cookies from
      * The optional fourth entry is a (Firefox) container name (``"none"`` for only cookies with no container)
      * The optional fifth entry is the domain to extract cookies for. Prefix it with a dot ``.`` to include cookies for subdomains. Has no effect when also specifying a container.

      .. code:: json

        ["firefox"]
        ["firefox", null, null, "Personal"]
        ["chromium", "Private", "kwallet", null, ".twitter.com"]


extractor.*.cookies-update
--------------------------
Type
    * ``bool``
    * |Path|_
Default
    ``true``
Description
    Export session cookies in cookies.txt format.

    * If this is a |Path|_, write cookies to the given file path.

    * If this is ``true`` and `extractor.*.cookies`_ specifies the |Path|_
      of a valid cookies.txt file, update its contents.


extractor.*.proxy
-----------------
Type
    * ``string``
    * ``object`` (`scheme` -> `proxy`)
Example
    .. code:: json

      "http://10.10.1.10:3128"

    .. code:: json

      {
          "http" : "http://10.10.1.10:3128",
          "https": "http://10.10.1.10:1080",
          "http://10.20.1.128": "http://10.10.1.10:5323"
      }

Description
    Proxy (or proxies) to be used for remote connections.

    * If this is a ``string``, it is the proxy URL for all
      outgoing requests.
    * If this is an ``object``, it is a scheme-to-proxy mapping to
      specify different proxy URLs for each scheme.
      It is also possible to set a proxy for a specific host by using
      ``scheme://host`` as key.
      See `Requests' proxy documentation`_ for more details.

    Note: If a proxy URLs does not include a scheme,
    ``http://`` is assumed.


extractor.*.source-address
--------------------------
Type
    * ``string``
    * ``list`` with 1 ``string`` and 1 ``integer`` as elements
Example
    * ``"192.168.178.20"``
    * ``["192.168.178.20", 8080]``
Description
    Client-side IP address to bind to.

    | Can be either a simple ``string`` with just the local IP address
    | or a ``list`` with IP and explicit port number as elements.


extractor.*.user-agent
----------------------
Type
    ``string``
Default
    ``"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"``
Description
    User-Agent header value to be used for HTTP requests.

    Setting this value to ``"browser"`` will try to automatically detect
    and use the User-Agent used by the system's default browser.

    Note: This option has no effect on
    `pixiv`, `e621`, and `mangadex`
    extractors, as these need specific values to function correctly.


extractor.*.browser
-------------------
Type
    ``string``
Default
    * ``"firefox"`` for ``patreon``, ``mangapark``, and ``mangasee``
    * ``null`` everywhere else
Example
    * ``"chrome:macos"``
Description
    Try to emulate a real browser (``firefox`` or ``chrome``)
    by using their default HTTP headers and TLS ciphers for HTTP requests.

    Optionally, the operating system used in the ``User-Agent`` header can be
    specified after a ``:`` (``windows``, ``linux``, or ``macos``).

    Note: ``requests`` and ``urllib3`` only support HTTP/1.1, while a real
    browser would use HTTP/2.


extractor.*.referer
-------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Send `Referer <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer>`__
    headers with all outgoing HTTP requests.

    If this is a ``string``, send it as Referer
    instead of the extractor's ``root`` domain.


extractor.*.headers
-------------------
Type
    ``object`` (`name` -> `value`)
Default
    .. code:: json

      {
          "User-Agent"     : "<extractor.*.user-agent>",
          "Accept"         : "*/*",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate",
          "Referer"        : "<extractor.*.referer>"
      }

Description
    Additional `HTTP headers <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers>`__
    to be sent with each HTTP request,

    To disable sending a header, set its value to ``null``.


extractor.*.ciphers
-------------------
Type
    ``list`` of ``strings``
Example
    .. code:: json

      ["ECDHE-ECDSA-AES128-GCM-SHA256",
       "ECDHE-RSA-AES128-GCM-SHA256",
       "ECDHE-ECDSA-CHACHA20-POLY1305",
       "ECDHE-RSA-CHACHA20-POLY1305"]

Description
    List of TLS/SSL cipher suites in
    `OpenSSL cipher list format <https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html>`__
    to be passed to
    `ssl.SSLContext.set_ciphers() <https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers>`__


extractor.*.tls12
-----------------
Type
    ``bool``
Default
    * ``true``
    * ``false`` for ``patreon``, ``pixiv:series``
Description
    Allow selecting TLS 1.2 cipher suites.

    Can be disabled to alter TLS fingerprints
    and potentially bypass Cloudflare blocks.


extractor.*.keywords
--------------------
Type
    ``object`` (`name` -> `value`)
Example
    ``{"type": "Pixel Art", "type_id": 123}``
Description
    Additional name-value pairs to be added to each metadata dictionary.


extractor.*.keywords-default
----------------------------
Type
    any
Default
    ``"None"``
Description
    Default value used for missing or undefined keyword names in
    `format strings`_.


extractor.*.metadata-url
------------------------
extractor.*.url-metadata
------------------------
Type
    ``string``
Description
    Insert a file's download URL into its metadata dictionary as the given name.

    For example, setting this option to ``"gdl_file_url"`` will cause a new
    metadata field with name ``gdl_file_url`` to appear, which contains the
    current file's download URL.
    This can then be used in `filenames <extractor.*.filename_>`_,
    with a ``metadata`` post processor, etc.


extractor.*.metadata-path
-------------------------
extractor.*.path-metadata
-------------------------
Type
    ``string``
Description
    Insert a reference to the current
    `PathFormat <https://github.com/mikf/gallery-dl/blob/v1.24.2/gallery_dl/path.py#L27>`__
    data structure into metadata dictionaries as the given name.

    For example, setting this option to ``"gdl_path"`` would make it possible
    to access the current file's filename as ``"{gdl_path.filename}"``.


extractor.*.metadata-extractor
------------------------------
extractor.*.extractor-metadata
------------------------------
Type
    ``string``
Description
    Insert a reference to the current
    `Extractor <https://github.com/mikf/gallery-dl/blob/v1.26.2/gallery_dl/extractor/common.py#L26>`__
    object into metadata dictionaries as the given name.


extractor.*.metadata-http
-------------------------
extractor.*.http-metadata
-------------------------
Type
    ``string``
Description
    Insert an ``object`` containing a file's HTTP headers and
    ``filename``, ``extension``, and ``date`` parsed from them
    into metadata dictionaries as the given name.

    For example, setting this option to ``"gdl_http"`` would make it possible
    to access the current file's ``Last-Modified`` header as ``"{gdl_http[Last-Modified]}"``
    and its parsed form as ``"{gdl_http[date]}"``.


extractor.*.metadata-version
----------------------------
extractor.*.version-metadata
----------------------------
Type
    ``string``
Description
    Insert an ``object`` containing gallery-dl's version info into
    metadata dictionaries as the given name.

    The content of the object is as follows:

    .. code:: json

        {
            "version"         : "string",
            "is_executable"   : "bool",
            "current_git_head": "string or null"
        }


extractor.*.category-transfer
-----------------------------
Type
    ``bool``
Default
    Extractor-specific
Description
    Transfer an extractor's (sub)category values to all child
    extractors spawned by it, to let them inherit their parent's
    config options.


extractor.*.blacklist & .whitelist
----------------------------------
Type
    ``list`` of ``strings``
Default
    ``["oauth", "recursive", "test"]`` + current extractor category
Example
    ``["imgur", "redgifs:user", "*:image"]``
Description
    A list of extractor identifiers to ignore (or allow)
    when spawning child extractors for unknown URLs,
    e.g. from ``reddit`` or ``plurk``.

    Each identifier can be

    * A category or basecategory name (``"imgur"``, ``"mastodon"``)
    * | A (base)category-subcategory pair, where both names are separated by a colon (``"redgifs:user"``).
      | Both names can be a `*` or left empty, matching all possible names (``"*:image"``, ``":user"``).

    Note: Any ``blacklist`` setting will automatically include
    ``"oauth"``, ``"recursive"``, and ``"test"``.


extractor.*.archive
-------------------
Type
    |Path|_
Default
    ``null``
Example
    ``"$HOME/.archives/{category}.sqlite3"``
Description
    File to store IDs of downloaded files in. Downloads of files
    already recorded in this archive file will be
    `skipped <extractor.*.skip_>`__.

    The resulting archive file is not a plain text file but an SQLite3
    database, as either lookup operations are significantly faster or
    memory requirements are significantly lower when the
    amount of stored IDs gets reasonably large.

    Note: Archive files that do not already exist get generated automatically.

    Note: Archive paths support regular `format string`_ replacements,
    but be aware that using external inputs for building local paths
    may pose a security risk.


extractor.*.archive-format
--------------------------
Type
    ``string``
Example
    ``"{id}_{offset}"``
Description
    An alternative `format string`_ to build archive IDs with.


extractor.*.archive-prefix
--------------------------
Type
    ``string``
Default
    ``"{category}"``
Description
    Prefix for archive IDs.


extractor.*.archive-pragma
--------------------------
Type
    ``list`` of ``strings``
Example
    ``["journal_mode=WAL", "synchronous=NORMAL"]``
Description
    A list of SQLite ``PRAGMA`` statements to run during archive initialization.

    See `<https://www.sqlite.org/pragma.html>`__
    for available ``PRAGMA`` statements and further details.


extractor.*.postprocessors
--------------------------
Type
    ``list`` of |Postprocessor Configuration|_ objects
Example
    .. code:: json

        [
            {
                "name": "zip" ,
                "compression": "store"
            },
            {
                "name": "exec",
                "command": ["/home/foobar/script", "{category}", "{image_id}"]
            }
        ]

Description
    A list of `post processors <Postprocessor Configuration_>`__
    to be applied to each downloaded file in the specified order.

    | Unlike other options, a |postprocessors|_ setting at a deeper level
      does not override any |postprocessors|_ setting at a lower level.
    | Instead, all post processors from all applicable |postprocessors|_
      settings get combined into a single list.

    For example

    * an ``mtime`` post processor at ``extractor.postprocessors``,
    * a ``zip`` post processor at ``extractor.pixiv.postprocessors``,
    * and using ``--exec``

    will run all three post processors - ``mtime``, ``zip``, ``exec`` -
    for each downloaded ``pixiv`` file.


extractor.*.postprocessor-options
---------------------------------
Type
    ``object`` (`name` -> `value`)
Example
    .. code:: json

        {
            "archive": null,
            "keep-files": true
        }

Description
    Additional `Postprocessor Options`_ that get added to each individual
    `post processor object <Postprocessor Configuration_>`__
    before initializing it and evaluating filters.


extractor.*.retries
-------------------
Type
    ``integer``
Default
    ``4``
Description
    Maximum number of times a failed HTTP request is retried before
    giving up, or ``-1`` for infinite retries.


extractor.*.retry-codes
-----------------------
Type
    ``list`` of ``integers``
Example
    ``[404, 429, 430]``
Description
    Additional `HTTP response status codes <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>`__
    to retry an HTTP request on.

    ``2xx`` codes (success responses) and
    ``3xx`` codes (redirection messages)
    will never be retried and always count as success,
    regardless of this option.

    ``5xx`` codes (server error responses)  will always be retried,
    regardless of this option.


extractor.*.timeout
-------------------
Type
    ``float``
Default
    ``30.0``
Description
    Amount of time (in seconds) to wait for a successful connection
    and response from a remote server.

    This value gets internally used as the |timeout|_ parameter for the
    |requests.request()|_ method.


extractor.*.verify
------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Controls whether to verify SSL/TLS certificates for HTTPS requests.

    If this is a ``string``, it must be the path to a CA bundle to use
    instead of the default certificates.

    This value gets internally used as the |verify|_ parameter for the
    |requests.request()|_ method.


extractor.*.download
--------------------
Type
    ``bool``
Default
    ``true``
Description
    Controls whether to download media files.

    Setting this to ``false`` won't download any files, but all other
    functions (`postprocessors`_, `download archive`_, etc.)
    will be executed as normal.


extractor.*.fallback
--------------------
Type
    ``bool``
Default
    ``true``
Description
    Use fallback download URLs when a download fails.


extractor.*.image-range
-----------------------
Type
    * ``string``
    * ``list`` of ``strings``
Examples
    * ``"10-20"``
    * ``"-5, 10, 30-50, 100-"``
    * ``"10:21, 30:51:2, :5, 100:"``
    * ``["-5", "10", "30-50", "100-"]``
Description
    Index range(s) selecting which files to download.

    These can be specified as

    * index: ``3`` (file number 3)
    * range: ``2-4`` (files 2, 3, and 4)
    * `slice <https://docs.python.org/3/library/functions.html#slice>`__: ``3:8:2`` (files 3, 5, and 7)

    | Arguments for range and slice notation are optional
      and will default to begin (``1``) or end (``sys.maxsize``) if omitted.
    | For example ``5-``, ``5:``, and ``5::`` all mean "Start at file number 5".

    Note: The index of the first file is ``1``.


extractor.*.chapter-range
-------------------------
Type
    ``string``
Description
    Like `image-range <extractor.*.image-range_>`__,
    but applies to delegated URLs like manga chapters, etc.


extractor.*.image-filter
------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Examples
    * ``"re.search(r'foo(bar)+', description)"``
    * ``["width >= 1200", "width/height > 1.2"]``
Description
    Python expression controlling which files to download.

    A file only gets downloaded when *all* of the given expressions evaluate to ``True``.

    Available values are the filename-specific ones listed by ``-K`` or ``-j``.


extractor.*.chapter-filter
--------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Examples
    * ``"lang == 'en'"``
    * ``["language == 'French'", "10 <= chapter < 20"]``
Description
    Like `image-filter <extractor.*.image-filter_>`__,
    but applies to delegated URLs like manga chapters, etc.


extractor.*.image-unique
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Ignore image URLs that have been encountered before during the
    current extractor run.


extractor.*.chapter-unique
--------------------------
Type
    ``bool``
Default
    ``false``
Description
    Like `image-unique <extractor.*.image-unique_>`__,
    but applies to delegated URLs like manga chapters, etc.


extractor.*.date-format
-----------------------
Type
    ``string``
Default
    ``"%Y-%m-%dT%H:%M:%S"``
Description
    Format string used to parse ``string`` values of
    `date-min` and `date-max`.

    See |strptime|_ for a list of formatting directives.

    Note: Despite its name, this option does **not** control how
    ``{date}`` metadata fields are formatted.
    To use a different formatting for those values other than the default
    ``%Y-%m-%d %H:%M:%S``, put |strptime|_ formatting directives
    after a colon ``:``, for example ``{date:%Y%m%d}``.


extractor.*.write-pages
-----------------------
Type
    * ``bool``
    * ``string``
Default
    ``false``
Description
    During data extraction,
    write received HTTP request data
    to enumerated files in the current working directory.

    Special values:

    * ``"all"``: Include HTTP request and response headers. Hide ``Authorization``, ``Cookie``, and ``Set-Cookie`` values.
    * ``"ALL"``: Include all HTTP request and response headers.
