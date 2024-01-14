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


Extractor-specific Options
==========================


extractor.artstation.external
-----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Try to follow external URLs of embedded players.


extractor.artstation.max-posts
------------------------------
Type
    ``integer``
Default
    ``null``
Description
    Limit the number of posts/projects to download.


extractor.artstation.search.pro-first
-------------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Enable the "Show Studio and Pro member artwork first" checkbox
    when retrieving search results.


extractor.aryion.recursive
--------------------------
Type
    ``bool``
Default
    ``true``
Description
    Controls the post extraction strategy.

    * ``true``: Start on users' main gallery pages and recursively
      descend into subfolders
    * ``false``: Get posts from "Latest Updates" pages


extractor.bbc.width
-------------------
Type
    ``integer``
Default
    ``1920``
Description
    Specifies the requested image width.

    This value must be divisble by 16 and gets rounded down otherwise.
    The maximum possible value appears to be ``1920``.


extractor.behance.modules
-------------------------
Type
    ``list`` of ``strings``
Default
    ``["image", "video", "mediacollection", "embed"]``
Description
    Selects which gallery modules to download from.

    Supported module types are
    ``image``, ``video``, ``mediacollection``, ``embed``, ``text``.


extractor.blogger.videos
------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download embedded videos hosted on https://www.blogger.com/


extractor.cyberdrop.domain
--------------------------
Type
    ``string``
Default
    ``null``
Example
    ``"cyberdrop.to"``
Description
    Specifies the domain used by ``cyberdrop`` regardless of input URL.

    Setting this option to ``"auto"``
    uses the same domain as a given input URL.


extractor.danbooru.external
---------------------------
Type
    ``bool``
Default
    ``false``
Description
    For unavailable or restricted posts,
    follow the ``source`` and download from there if possible.


extractor.danbooru.ugoira
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Controls the download target for Ugoira posts.

    * ``true``: Original ZIP archives
    * ``false``: Converted video files


extractor.[Danbooru].metadata
-----------------------------
Type
    * ``bool``
    * ``string``
    * ``list`` of ``strings``
Default
    ``false``
Example
    * ``replacements,comments,ai_tags``
    * ``["replacements", "comments", "ai_tags"]``
Description
    Extract additional metadata
    (notes, artist commentary, parent, children, uploader)

    It is possible to specify a custom list of metadata includes.
    See `available_includes <https://github.com/danbooru/danbooru/blob/2cf7baaf6c5003c1a174a8f2d53db010cf05dca7/app/models/post.rb#L1842-L1849>`__
    for possible field names. ``aibooru`` also supports ``ai_metadata``.

    Note: This requires 1 additional HTTP request per 200-post batch.


extractor.[Danbooru].threshold
------------------------------
Type
    * ``string``
    * ``integer``
Default
    ``"auto"``
Description
    Stop paginating over API results if the length of a batch of returned
    posts is less than the specified number. Defaults to the per-page limit
    of the current instance, which is 200.

    Note: Changing this setting is normally not necessary. When the value is
    greater than the per-page limit, gallery-dl will stop after the first
    batch. The value cannot be less than 1.


extractor.derpibooru.api-key
----------------------------
Type
    ``string``
Default
    ``null``
Description
    Your `Derpibooru API Key <https://derpibooru.org/registrations/edit>`__,
    to use your account's browsing settings and filters.


extractor.derpibooru.filter
---------------------------
Type
    ``integer``
Default
    ``56027`` (`Everything <https://derpibooru.org/filters/56027>`_ filter)
Description
    The content filter ID to use.

    Setting an explicit filter ID overrides any default filters and can be used
    to access 18+ content without `API Key <extractor.derpibooru.api-key_>`_.

    See `Filters <https://derpibooru.org/filters>`_ for details.


extractor.deviantart.auto-watch
-------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Automatically watch users when encountering "Watchers-Only Deviations"
    (requires a `refresh-token <extractor.deviantart.refresh-token_>`_).


extractor.deviantart.auto-unwatch
---------------------------------
Type
    ``bool``
Default
    ``false``
Description
    After watching a user through `auto-watch <extractor.deviantart.auto-watch_>`_,
    unwatch that user at the end of the current extractor run.


extractor.deviantart.comments
-----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract ``comments`` metadata.


extractor.deviantart.extra
--------------------------
Type
    ``bool``
Default
    ``false``
Description
    Download extra Sta.sh resources from
    description texts and journals.

    Note: Enabling this option also enables deviantart.metadata_.


extractor.deviantart.flat
-------------------------
Type
    ``bool``
Default
    ``true``
Description
    Select the directory structure created by the Gallery- and
    Favorite-Extractors.

    * ``true``: Use a flat directory structure.
    * ``false``: Collect a list of all gallery-folders or
      favorites-collections and transfer any further work to other
      extractors (``folder`` or ``collection``), which will then
      create individual subdirectories for each of them.

      Note: Going through all gallery folders will not be able to
      fetch deviations which aren't in any folder.


extractor.deviantart.folders
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Provide a ``folders`` metadata field that contains the names of all
    folders a deviation is present in.

    Note: Gathering this information requires a lot of API calls.
    Use with caution.


extractor.deviantart.group
--------------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Check whether the profile name in a given URL
    belongs to a group or a regular user.

    When disabled, assume every given profile name
    belongs to a regular user.

    Special values:

    * ``"skip"``: Skip groups


extractor.deviantart.include
----------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"gallery"``
Example
    * ``"favorite,journal,scraps"``
    * ``["favorite", "journal", "scraps"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"avatar"``,
    ``"background"``,
    ``"gallery"``,
    ``"scraps"``,
    ``"journal"``,
    ``"favorite"``,
    ``"status"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.deviantart.intermediary
---------------------------------
Type
    ``bool``
Default
    ``true``
Description
    For older non-downloadable images,
    download a higher-quality ``/intermediary/`` version.


extractor.deviantart.journals
-----------------------------
Type
    ``string``
Default
    ``"html"``
Description
    Selects the output format for textual content. This includes journals,
    literature and status updates.

    * ``"html"``: HTML with (roughly) the same layout as on DeviantArt.
    * ``"text"``: Plain text with image references and HTML tags removed.
    * ``"none"``: Don't download textual content.


extractor.deviantart.jwt
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Update `JSON Web Tokens <https://jwt.io/>`__ (the ``token`` URL parameter)
    of otherwise non-downloadable, low-resolution images
    to be able to download them in full resolution.

    Note: No longer functional as of 2023-10-11


extractor.deviantart.mature
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Enable mature content.

    This option simply sets the |mature_content|_ parameter for API
    calls to either ``"true"`` or ``"false"`` and does not do any other
    form of content filtering.


extractor.deviantart.metadata
-----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Request extended metadata for deviation objects to additionally provide
    ``description``, ``tags``, ``license`` and ``is_watching`` fields.


extractor.deviantart.original
-----------------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Download original files if available.

    Setting this option to ``"images"`` only downloads original
    files if they are images and falls back to preview versions for
    everything else (archives, etc.).


extractor.deviantart.pagination
-------------------------------
Type
    ``string``
Default
    ``"api"``
Description
    Controls when to stop paginating over API results.

    * ``"api"``: Trust the API and stop when ``has_more`` is ``false``.
    * ``"manual"``: Disregard ``has_more`` and only stop when a batch of results is empty.


extractor.deviantart.public
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Use a public access token for API requests.

    Disable this option to *force* using a private token for all requests
    when a `refresh token <extractor.deviantart.refresh-token_>`__ is provided.


extractor.deviantart.quality
----------------------------
Type
    ``integer``
Default
    ``100``
Description
    JPEG quality level of newer images for which
    an original file download is not available.

    Note: Only has an effect when `deviantart.jwt <extractor.deviantart.jwt_>`__ is disabled.


extractor.deviantart.refresh-token
----------------------------------
Type
    ``string``
Default
    ``null``
Description
    The ``refresh-token`` value you get from
    `linking your DeviantArt account to gallery-dl <OAuth_>`__.

    Using a ``refresh-token`` allows you to access private or otherwise
    not publicly available deviations.

    Note: The ``refresh-token`` becomes invalid
    `after 3 months <https://www.deviantart.com/developers/authentication#refresh>`__
    or whenever your `cache file <cache.file_>`__ is deleted or cleared.


extractor.deviantart.wait-min
-----------------------------
Type
    ``integer``
Default
    ``0``
Description
    Minimum wait time in seconds before API requests.


extractor.deviantart.avatar.formats
-----------------------------------
Type
    ``list`` of ``strings``
Example
    ``["original.jpg", "big.jpg", "big.gif", ".png"]``
Description
    Avatar URL formats to return.

    | Each format is parsed as ``SIZE.EXT``.
    | Leave ``SIZE`` empty to download the regular, small avatar format.


extractor.[E621].metadata
-------------------------
Type
    * ``bool``
    * ``string``
    * ``list`` of ``strings``
Default
    ``false``
Example
    * ``notes,pools``
    * ``["notes", "pools"]``
Description
    Extract additional metadata (notes, pool metadata) if available.

    Note: This requires 0-2 additional HTTP requests per post.


extractor.[E621].threshold
--------------------------
Type
    * ``string``
    * ``integer``
Default
    ``"auto"``
Description
    Stop paginating over API results if the length of a batch of returned
    posts is less than the specified number. Defaults to the per-page limit
    of the current instance, which is 320.

    Note: Changing this setting is normally not necessary. When the value is
    greater than the per-page limit, gallery-dl will stop after the first
    batch. The value cannot be less than 1.


extractor.exhentai.domain
-------------------------
Type
    ``string``
Default
    ``"auto"``
Description
    * ``"auto"``: Use ``e-hentai.org`` or ``exhentai.org``
      depending on the input URL
    * ``"e-hentai.org"``: Use ``e-hentai.org`` for all URLs
    * ``"exhentai.org"``: Use ``exhentai.org`` for all URLs


extractor.exhentai.fallback-retries
-----------------------------------
Type
    ``integer``
Default
    ``2``
Description
    Number of times a failed image gets retried
    or ``-1`` for infinite retries.


extractor.exhentai.fav
----------------------
Type
    ``string``
Example
    ``"4"``
Description
    After downloading a gallery,
    add it to your account's favorites as the given category number.

    Note: Set this to `"favdel"` to remove galleries from your favorites.

    Note: This will remove any Favorite Notes when applied
    to already favorited galleries.


extractor.exhentai.gp
---------------------
Type
    ``string``
Default
    ``"resized"``
Description
    Selects how to handle "you do not have enough GP" errors.

    * `"resized"`: Continue downloading `non-original <extractor.exhentai.original_>`__ images.
    * `"stop"`: Stop the current extractor run.
    * `"wait"`: Wait for user input before retrying the current image.


extractor.exhentai.limits
-------------------------
Type
    ``integer``
Default
    ``null``
Description
    Sets a custom image download limit and
    stops extraction when it gets exceeded.


extractor.exhentai.metadata
---------------------------
Type
    ``bool``
Default
    ``false``
Description
    Load extended gallery metadata from the
    `API <https://ehwiki.org/wiki/API#Gallery_Metadata>`_.

    Adds ``archiver_key``, ``posted``, and ``torrents``.
    Makes ``date`` and ``filesize`` more precise.


extractor.exhentai.original
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download full-sized original images if available.


extractor.exhentai.source
-------------------------
Type
    ``string``
Default
    ``"gallery"``
Description
    Selects an alternative source to download files from.

    * ``"hitomi"``:  Download the corresponding gallery from ``hitomi.la``


extractor.fanbox.embeds
-----------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Control behavior on embedded content from external sites.

    * ``true``: Extract embed URLs and download them if supported
      (videos are not downloaded).
    * ``"ytdl"``: Like ``true``, but let `youtube-dl`_ handle video
      extraction and download for YouTube, Vimeo and SoundCloud embeds.
    * ``false``: Ignore embeds.


extractor.fanbox.metadata
-------------------------
Type
    * ``bool``
    * ``string``
    * ``list`` of ``strings``
Default
    ``false``
Example
    * ``user,plan``
    * ``["user", "plan"]``
Description
    Extract ``plan`` and extended ``user`` metadata.


extractor.flickr.access-token & .access-token-secret
----------------------------------------------------
Type
    ``string``
Default
    ``null``
Description
    The ``access_token`` and ``access_token_secret`` values you get
    from `linking your Flickr account to gallery-dl <OAuth_>`__.


extractor.flickr.exif
---------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch `exif` and `camera` metadata for each photo.

    Note: This requires 1 additional API call per photo.


extractor.flickr.metadata
-------------------------
Type
    * ``bool``
    * ``string``
    * ``list`` of ``strings``
Default
    ``false``
Example
    * ``license,last_update,machine_tags``
    * ``["license", "last_update", "machine_tags"]``
Description
    Extract additional metadata
    (license, date_taken, original_format, last_update, geo, machine_tags, o_dims)

    It is possible to specify a custom list of metadata includes.
    See `the extras parameter <https://www.flickr.com/services/api/flickr.people.getPhotos.html>`__
    in `Flickr API docs <https://www.flickr.com/services/api/>`__
    for possible field names.


extractor.flickr.videos
-----------------------
Type
    ``bool``
Default
    ``true``
Description
    Extract and download videos.


extractor.flickr.size-max
--------------------------
Type
    * ``integer``
    * ``string``
Default
    ``null``
Description
    Sets the maximum allowed size for downloaded images.

    * If this is an ``integer``, it specifies the maximum image dimension
      (width and height) in pixels.
    * If this is a ``string``, it should be one of Flickr's format specifiers
      (``"Original"``, ``"Large"``, ... or ``"o"``, ``"k"``, ``"h"``,
      ``"l"``, ...) to use as an upper limit.


extractor.furaffinity.descriptions
----------------------------------
Type
    ``string``
Default
    ``"text"``
Description
    Controls the format of ``description`` metadata fields.

    * ``"text"``: Plain text with HTML tags removed
    * ``"html"``: Raw HTML content


extractor.furaffinity.external
------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Follow external URLs linked in descriptions.


extractor.furaffinity.include
-----------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"gallery"``
Example
    * ``"scraps,favorite"``
    * ``["scraps", "favorite"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"gallery"``, ``"scraps"``, ``"favorite"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.furaffinity.layout
----------------------------
Type
    ``string``
Default
    ``"auto"``
Description
    Selects which site layout to expect when parsing posts.

    * ``"auto"``: Automatically differentiate between ``"old"`` and ``"new"``
    * ``"old"``: Expect the *old* site layout
    * ``"new"``: Expect the *new* site layout


extractor.gelbooru.api-key & .user-id
-------------------------------------
Type
    ``string``
Default
    ``null``
Description
    Values from the API Access Credentials section found at the bottom of your
    `Account Options <https://gelbooru.com/index.php?page=account&s=options>`__
    page.


extractor.generic.enabled
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Match **all** URLs not otherwise supported by gallery-dl,
    even ones without a ``generic:`` prefix.


extractor.gofile.api-token
--------------------------
Type
    ``string``
Default
    ``null``
Description
    API token value found at the bottom of your `profile page <https://gofile.io/myProfile>`__.

    If not set, a temporary guest token will be used.


extractor.gofile.website-token
------------------------------
Type
    ``string``
Description
    API token value used during API requests.

    An invalid or not up-to-date value
    will result in ``401 Unauthorized`` errors.

    Keeping this option unset will use an extra HTTP request
    to attempt to fetch the current value used by gofile.


extractor.gofile.recursive
--------------------------
Type
    ``bool``
Default
    ``false``
Description
    Recursively download files from subfolders.


extractor.hentaifoundry.include
-------------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"pictures"``
Example
    * ``"scraps,stories"``
    * ``["scraps", "stories"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"pictures"``, ``"scraps"``, ``"stories"``, ``"favorite"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.hitomi.format
-----------------------
Type
    ``string``
Default
    ``"webp"``
Description
    Selects which image format to download.

    Available formats are ``"webp"`` and ``"avif"``.

    ``"original"`` will try to download the original ``jpg`` or ``png`` versions,
    but is most likely going to fail with ``403 Forbidden`` errors.


extractor.imagechest.access-token
---------------------------------
Type
    ``string``
Description
    Your personal Image Chest access token.

    These tokens allow using the API instead of having to scrape HTML pages,
    providing more detailed metadata.
    (``date``, ``description``, etc)

    See https://imgchest.com/docs/api/1.0/general/authorization
    for instructions on how to generate such a token.


extractor.imgur.client-id
-------------------------
Type
    ``string``
Description
    Custom Client ID value for API requests.


extractor.imgur.mp4
-------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Controls whether to choose the GIF or MP4 version of an animation.

    * ``true``: Follow Imgur's advice and choose MP4 if the
      ``prefer_video`` flag in an image's metadata is set.
    * ``false``: Always choose GIF.
    * ``"always"``: Always choose MP4.


extractor.inkbunny.orderby
--------------------------
Type
    ``string``
Default
    ``"create_datetime"``
Description
    Value of the ``orderby`` parameter for submission searches.

    (See `API#Search <https://wiki.inkbunny.net/wiki/API#Search>`__
    for details)


extractor.instagram.api
-----------------------
Type
    ``string``
Default
    ``"rest"``
Description
    Selects which API endpoints to use.

    * ``"rest"``: REST API - higher-resolution media
    * ``"graphql"``: GraphQL API - lower-resolution media


extractor.instagram.include
---------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"posts"``
Example
    * ``"stories,highlights,posts"``
    * ``["stories", "highlights", "posts"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"posts"``,
    ``"reels"``,
    ``"tagged"``,
    ``"stories"``,
    ``"highlights"``,
    ``"avatar"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.instagram.metadata
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Provide extended ``user`` metadata even when referring to a user by ID,
    e.g. ``instagram.com/id:12345678``.

    Note: This metadata is always available when referring to a user by name,
    e.g. ``instagram.com/USERNAME``.


extractor.instagram.order-files
-------------------------------
Type
    ``string``
Default
    ``"asc"``
Description
    Controls the order in which files of each post are returned.

    * ``"asc"``: Same order as displayed in a post
    * ``"desc"``: Reverse order as displayed in a post
    * ``"reverse"``: Same as ``"desc"``

    Note: This option does *not* affect ``{num}``.
    To enumerate files in reverse order, use ``count - num + 1``.


extractor.instagram.order-posts
-------------------------------
Type
    ``string``
Default
    ``"asc"``
Description
    Controls the order in which posts are returned.

    * ``"asc"``: Same order as displayed
    * ``"desc"``: Reverse order as displayed
    * ``"id"`` or ``"id_asc"``: Ascending order by ID
    * ``"id_desc"``: Descending order by ID
    * ``"reverse"``: Same as ``"desc"``

    Note: This option only affects ``highlights``.


extractor.instagram.previews
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Download video previews.


extractor.instagram.videos
--------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download video files.


extractor.itaku.videos
----------------------
Type
    ``bool``
Default
    ``true``
Description
    Download video files.


extractor.kemonoparty.comments
------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract ``comments`` metadata.

    Note: This requires 1 additional HTTP request per post.


extractor.kemonoparty.duplicates
--------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Controls how to handle duplicate files in a post.

    * ``true``: Download duplicates
    * ``false``: Ignore duplicates


extractor.kemonoparty.dms
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract a user's direct messages as ``dms`` metadata.


extractor.kemonoparty.favorites
-------------------------------
Type
    ``string``
Default
    ``artist``
Description
    Determines the type of favorites to be downloaded.

    Available types are ``artist``, and ``post``.


extractor.kemonoparty.files
---------------------------
Type
    ``list`` of ``strings``
Default
    ``["attachments", "file", "inline"]``
Description
    Determines the type and order of files to be downloaded.

    Available types are ``file``, ``attachments``, and ``inline``.


extractor.kemonoparty.max-posts
-------------------------------
Type
    ``integer``
Default
    ``null``
Description
    Limit the number of posts to download.


extractor.kemonoparty.metadata
------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract ``username`` metadata.


extractor.kemonoparty.revisions
-------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract post revisions.

    Note: This requires 1 additional HTTP request per post.


extractor.khinsider.format
--------------------------
Type
    ``string``
Default
    ``"mp3"``
Description
    The name of the preferred file format to download.

    Use ``"all"`` to download all available formats,
    or a (comma-separated) list to select multiple formats.

    If the selected format is not available,
    the first in the list gets chosen (usually `mp3`).
