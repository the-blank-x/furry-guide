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


extractor.lolisafe.domain
-------------------------
Type
    ``string``
Default
    ``null``
Description
    Specifies the domain used by a ``lolisafe`` extractor
    regardless of input URL.

    Setting this option to ``"auto"``
    uses the same domain as a given input URL.


extractor.luscious.gif
----------------------
Type
    ``bool``
Default
    ``false``
Description
    Format in which to download animated images.

    Use ``true`` to download animated images as gifs and ``false``
    to download as mp4 videos.


extractor.mangadex.api-server
-----------------------------
Type
    ``string``
Default
    ``"https://api.mangadex.org"``
Description
    The server to use for API requests.


extractor.mangadex.api-parameters
---------------------------------
Type
    ``object`` (`name` -> `value`)
Example
    ``{"order[updatedAt]": "desc"}``
Description
    Additional query parameters to send when fetching manga chapters.

    (See `/manga/{id}/feed <https://api.mangadex.org/docs/swagger.html#/Manga/get-manga-id-feed>`__
    and `/user/follows/manga/feed <https://api.mangadex.org/docs/swagger.html#/Feed/get-user-follows-manga-feed>`__)


extractor.mangadex.lang
-----------------------
Type
    * ``string``
    * ``list`` of ``strings``
Example
    * ``"en"``
    * ``"fr,it"``
    * ``["fr", "it"]``
Description
    `ISO 639-1 <https://en.wikipedia.org/wiki/ISO_639-1>`__ language codes
    to filter chapters by.


extractor.mangadex.ratings
--------------------------
Type
    ``list`` of ``strings``
Default
    ``["safe", "suggestive", "erotica", "pornographic"]``
Description
    List of acceptable content ratings for returned chapters.


extractor.mangapark.source
--------------------------
Type
    * ``string``
    * ``integer``
Example
    * ``"koala:en"``
    * ``15150116``
Description
    Select chapter source and language for a manga.

    | The general syntax is ``"<source name>:<ISO 639-1 language code>"``.
    | Both are optional, meaning ``"koala"``, ``"koala:"``, ``":en"``,
      or even just ``":"`` are possible as well.

    Specifying the numeric ``ID`` of a source is also supported.


extractor.[mastodon].access-token
---------------------------------
Type
    ``string``
Default
    ``null``
Description
    The ``access-token`` value you get from `linking your account to
    gallery-dl <OAuth_>`__.

    Note: gallery-dl comes with built-in tokens for ``mastodon.social``,
    ``pawoo`` and ``baraag``. For other instances, you need to obtain an
    ``access-token`` in order to use usernames in place of numerical
    user IDs.


extractor.[mastodon].reblogs
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from reblogged posts.


extractor.[mastodon].replies
----------------------------
Type
    ``bool``
Default
    ``true``
Description
    Fetch media from replies to other posts.


extractor.[mastodon].text-posts
-------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Also emit metadata for text-only posts without media content.


extractor.[misskey].access-token
--------------------------------
Type
    ``string``
Description
    Your access token, necessary to fetch favorited notes.


extractor.[misskey].renotes
---------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from renoted notes.


extractor.[misskey].replies
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Fetch media from replies to other notes.


extractor.[moebooru].pool.metadata
----------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract extended ``pool`` metadata.

    Note: Not supported by all ``moebooru`` instances.


extractor.newgrounds.flash
--------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download original Adobe Flash animations instead of pre-rendered videos.


extractor.newgrounds.format
---------------------------
Type
    ``string``
Default
    ``"original"``
Example
    ``"720p"``
Description
    Selects the preferred format for video downloads.

    If the selected format is not available,
    the next smaller one gets chosen.


extractor.newgrounds.include
----------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"art"``
Example
    * ``"movies,audio"``
    * ``["movies", "audio"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"art"``, ``"audio"``, ``"games"``, ``"movies"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.nijie.include
-----------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"illustration,doujin"``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"illustration"``, ``"doujin"``, ``"favorite"``, ``"nuita"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.nitter.quoted
-----------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from quoted Tweets.


extractor.nitter.retweets
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from Retweets.


extractor.nitter.videos
-----------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Control video download behavior.

    * ``true``: Download videos
    * ``"ytdl"``: Download videos using `youtube-dl`_
    * ``false``: Skip video Tweets


extractor.oauth.browser
-----------------------
Type
    ``bool``
Default
    ``true``
Description
    Controls how a user is directed to an OAuth authorization page.

    * ``true``: Use Python's |webbrowser.open()|_ method to automatically
      open the URL in the user's default browser.
    * ``false``: Ask the user to copy & paste an URL from the terminal.


extractor.oauth.cache
---------------------
Type
    ``bool``
Default
    ``true``
Description
    Store tokens received during OAuth authorizations
    in `cache <cache.file_>`__.


extractor.oauth.host
--------------------
Type
    ``string``
Default
    ``"localhost"``
Description
    Host name / IP address to bind to during OAuth authorization.


extractor.oauth.port
--------------------
Type
    ``integer``
Default
    ``6414``
Description
    Port number to listen on during OAuth authorization.

    Note: All redirects will go to port ``6414``, regardless
    of the port specified here. You'll have to manually adjust the
    port number in your browser's address bar when using a different
    port than the default.


extractor.paheal.metadata
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract additional metadata (``source``, ``uploader``)

    Note: This requires 1 additional HTTP request per post.


extractor.patreon.files
-----------------------
Type
    ``list`` of ``strings``
Default
    ``["images", "image_large", "attachments", "postfile", "content"]``
Description
    Determines the type and order of files to be downloaded.

    Available types are
    ``postfile``, ``images``, ``image_large``, ``attachments``, and ``content``.


extractor.photobucket.subalbums
-------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download subalbums.


extractor.pillowfort.external
-----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Follow links to external sites, e.g. Twitter,


extractor.pillowfort.inline
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Extract inline images.


extractor.pillowfort.reblogs
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract media from reblogged posts.


extractor.pinterest.domain
--------------------------
Type
    ``string``
Default
    ``"auto"``
Description
    Specifies the domain used by ``pinterest`` extractors.

    Setting this option to ``"auto"``
    uses the same domain as a given input URL.


extractor.pinterest.sections
----------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include pins from board sections.


extractor.pinterest.videos
--------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download from video pins.


extractor.pixeldrain.api-key
----------------------------
Type
    ``string``
Description
    Your account's `API key <https://pixeldrain.com/user/api_keys>`__


extractor.pixiv.include
-----------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"artworks"``
Example
    * ``"avatar,background,artworks"``
    * ``["avatar", "background", "artworks"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"artworks"``,
    ``"avatar"``,
    ``"background"``,
    ``"favorite"``,
    ``"novel-user"``,
    ``"novel-bookmark"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.pixiv.refresh-token
-----------------------------
Type
    ``string``
Description
    The ``refresh-token`` value you get
    from running ``gallery-dl oauth:pixiv`` (see OAuth_) or
    by using a third-party tool like
    `gppt <https://github.com/eggplants/get-pixivpy-token>`__.


extractor.pixiv.embeds
----------------------
Type
    ``bool``
Default
    ``false``
Description
    Download images embedded in novels.


extractor.pixiv.novel.full-series
---------------------------------
Type
    ``bool``
Default
    ``false``
Description
    When downloading a novel being part of a series,
    download all novels of that series.


extractor.pixiv.metadata
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch extended ``user`` metadata.


extractor.pixiv.metadata-bookmark
---------------------------------
Type
    ``bool``
Default
    ``false``
Description
    For works bookmarked by
    `your own account <extractor.pixiv.refresh-token_>`__,
    fetch bookmark tags as ``tags_bookmark`` metadata.

    Note: This requires 1 additional API call per bookmarked post.


extractor.pixiv.work.related
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Also download related artworks.


extractor.pixiv.tags
--------------------
Type
    ``string``
Default
    ``"japanese"``
Description
    Controls the ``tags`` metadata field.

    * `"japanese"`: List of Japanese tags
    * `"translated"`: List of translated tags
    * `"original"`: Unmodified list with both Japanese and translated tags


extractor.pixiv.ugoira
----------------------
Type
    ``bool``
Default
    ``true``
Description
    Download Pixiv's Ugoira animations or ignore them.

    These animations come as a ``.zip`` file containing all
    animation frames in JPEG format.

    Use an `ugoira` post processor to convert them
    to watchable videos. (Example__)

.. __: https://github.com/mikf/gallery-dl/blob/v1.12.3/docs/gallery-dl-example.conf#L9-L14


extractor.pixiv.max-posts
-------------------------
Type
    ``integer``
Default
    ``0``
Description
    When downloading galleries, this sets the maximum number of posts to get.
    A value of ``0`` means no limit.


extractor.plurk.comments
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Also search Plurk comments for URLs.


extractor.[postmill].save-link-post-body
----------------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Whether or not to save the body for link/image posts.


extractor.reactor.gif
---------------------
Type
    ``bool``
Default
    ``false``
Description
    Format in which to download animated images.

    Use ``true`` to download animated images as gifs and ``false``
    to download as mp4 videos.


extractor.readcomiconline.captcha
---------------------------------
Type
    ``string``
Default
    ``"stop"``
Description
    Controls how to handle redirects to CAPTCHA pages.

    * ``"stop``: Stop the current extractor run.
    * ``"wait``: Ask the user to solve the CAPTCHA and wait.


extractor.readcomiconline.quality
---------------------------------
Type
    ``string``
Default
    ``"auto"``
Description
    Sets the ``quality`` query parameter of issue pages. (``"lq"`` or ``"hq"``)

    ``"auto"`` uses the quality parameter of the input URL
    or ``"hq"`` if not present.


extractor.reddit.comments
-------------------------
Type
    ``integer``
Default
    ``0``
Description
    The value of the ``limit`` parameter when loading
    a submission and its comments.
    This number (roughly) specifies the total amount of comments
    being retrieved with the first API call.

    Reddit's internal default and maximum values for this parameter
    appear to be 200 and 500 respectively.

    The value ``0`` ignores all comments and significantly reduces the
    time required when scanning a subreddit.


extractor.reddit.morecomments
-----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Retrieve additional comments by resolving the ``more`` comment
    stubs in the base comment tree.

    Note: This requires 1 additional API call for every 100 extra comments.


extractor.reddit.date-min & .date-max
-------------------------------------
Type
    |Date|_
Default
    ``0`` and ``253402210800`` (timestamp of |datetime.max|_)
Description
    Ignore all submissions posted before/after this date.


extractor.reddit.id-min & .id-max
---------------------------------
Type
    ``string``
Example
    ``"6kmzv2"``
Description
    Ignore all submissions posted before/after the submission with this ID.


extractor.reddit.previews
-------------------------
Type
    ``bool``
Default
    ``true``
Description
    For failed downloads from external URLs / child extractors,
    download Reddit's preview image/video if available.


extractor.reddit.recursion
--------------------------
Type
    ``integer``
Default
    ``0``
Description
    Reddit extractors can recursively visit other submissions
    linked to in the initial set of submissions.
    This value sets the maximum recursion depth.

    Special values:

    * ``0``: Recursion is disabled
    * ``-1``: Infinite recursion (don't do this)


extractor.reddit.refresh-token
------------------------------
Type
    ``string``
Default
    ``null``
Description
    The ``refresh-token`` value you get from
    `linking your Reddit account to gallery-dl <OAuth_>`__.

    Using a ``refresh-token`` allows you to access private or otherwise
    not publicly available subreddits, given that your account is
    authorized to do so,
    but requests to the reddit API are going to be rate limited
    at 600 requests every 10 minutes/600 seconds.


extractor.reddit.videos
-----------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Control video download behavior.

    * ``true``: Download videos and use `youtube-dl`_ to handle
      HLS and DASH manifests
    * ``"ytdl"``: Download videos and let `youtube-dl`_ handle all of
      video extraction and download
    * ``"dash"``: Extract DASH manifest URLs and use `youtube-dl`_
      to download and merge them. (*)
    * ``false``: Ignore videos

    (*)
    This saves 1 HTTP request per video
    and might potentially be able to download otherwise deleted videos,
    but it will not always get the best video quality available.


extractor.redgifs.format
------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``["hd", "sd", "gif"]``
Description
    List of names of the preferred animation format, which can be
    ``"hd"``,
    ``"sd"``,
    ``"gif"``,
    ``"thumbnail"``,
    ``"vthumbnail"``, or
    ``"poster"``.

    If a selected format is not available, the next one in the list will be
    tried until an available format is found.

    If the format is given as ``string``, it will be extended with
    ``["hd", "sd", "gif"]``. Use a list with one element to
    restrict it to only one possible format.


extractor.sankaku.refresh
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Refresh download URLs before they expire.


extractor.sankakucomplex.embeds
-------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Download video embeds from external sites.


extractor.sankakucomplex.videos
-------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download videos.


extractor.skeb.article
----------------------
Type
    ``bool``
Default
    ``false``
Description
    Download article images.


extractor.skeb.sent-requests
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Download sent requests.


extractor.skeb.thumbnails
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Download thumbnails.


extractor.skeb.search.filters
-----------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``["genre:art", "genre:voice", "genre:novel", "genre:video", "genre:music", "genre:correction"]``
Example
    ``"genre:music OR genre:voice"``
Description
    Filters used during searches.


extractor.smugmug.videos
------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download video files.


extractor.steamgriddb.animated
------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include animated assets when downloading from a list of assets.


extractor.steamgriddb.epilepsy
------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include assets tagged with epilepsy when downloading from a list of assets.


extractor.steamgriddb.dimensions
--------------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"all"``
Examples
    * ``"1024x512,512x512"``
    * ``["460x215", "920x430"]``
Description
    Only include assets that are in the specified dimensions. ``all`` can be
    used to specify all dimensions. Valid values are:

    * Grids: ``460x215``, ``920x430``, ``600x900``, ``342x482``, ``660x930``,
      ``512x512``, ``1024x1024``
    * Heroes: ``1920x620``, ``3840x1240``, ``1600x650``
    * Logos: N/A (will be ignored)
    * Icons: ``8x8``, ``10x10``, ``14x14``, ``16x16``, ``20x20``, ``24x24``,
      ``28x28``, ``32x32``, ``35x35``, ``40x40``, ``48x48``, ``54x54``,
      ``56x56``, ``57x57``, ``60x60``, ``64x64``, ``72x72``, ``76x76``,
      ``80x80``, ``90x90``, ``96x96``, ``100x100``, ``114x114``, ``120x120``,
      ``128x128``, ``144x144``, ``150x150``, ``152x152``, ``160x160``,
      ``180x180``, ``192x192``, ``194x194``, ``256x256``, ``310x310``,
      ``512x512``, ``768x768``, ``1024x1024``


extractor.steamgriddb.file-types
--------------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"all"``
Examples
    * ``"png,jpeg"``
    * ``["jpeg", "webp"]``
Description
    Only include assets that are in the specified file types. ``all`` can be
    used to specifiy all file types. Valid values are:

    * Grids: ``png``, ``jpeg``, ``jpg``, ``webp``
    * Heroes: ``png``, ``jpeg``, ``jpg``, ``webp``
    * Logos: ``png``, ``webp``
    * Icons: ``png``, ``ico``


extractor.steamgriddb.download-fake-png
---------------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download fake PNGs alongside the real file.


extractor.steamgriddb.humor
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include assets tagged with humor when downloading from a list of assets.


extractor.steamgriddb.languages
-------------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"all"``
Examples
    * ``"en,km"``
    * ``["fr", "it"]``
Description
    Only include assets that are in the specified languages. ``all`` can be
    used to specifiy all languages. Valid values are `ISO 639-1 <https://en.wikipedia.org/wiki/ISO_639-1>`__
    language codes.


extractor.steamgriddb.nsfw
--------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include assets tagged with adult content when downloading from a list of assets.


extractor.steamgriddb.sort
--------------------------
Type
    ``string``
Default
    ``score_desc``
Description
    Set the chosen sorting method when downloading from a list of assets. Can be one of:

    * ``score_desc`` (Highest Score (Beta))
    * ``score_asc`` (Lowest Score (Beta))
    * ``score_old_desc`` (Highest Score (Old))
    * ``score_old_asc`` (Lowest Score (Old))
    * ``age_desc`` (Newest First)
    * ``age_asc`` (Oldest First)


extractor.steamgriddb.static
----------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include static assets when downloading from a list of assets.


extractor.steamgriddb.styles
----------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``all``
Examples
    * ``white,black``
    * ``["no_logo", "white_logo"]``
Description
    Only include assets that are in the specified styles. ``all`` can be used
    to specify all styles. Valid values are:

    * Grids: ``alternate``, ``blurred``, ``no_logo``, ``material``, ``white_logo``
    * Heroes: ``alternate``, ``blurred``, ``material``
    * Logos: ``official``, ``white``, ``black``, ``custom``
    * Icons: ``official``, ``custom``


extractor.steamgriddb.untagged
------------------------------
Type
    ``bool``
Default
    ``true``
Description
    Include untagged assets when downloading from a list of assets.


extractor.[szurubooru].username & .token
----------------------------------------
Type
    ``string``
Description
    Username and login token of your account to access private resources.

    To generate a token, visit ``/user/USERNAME/list-tokens``
    and click ``Create Token``.


extractor.tumblr.avatar
-----------------------
Type
    ``bool``
Default
    ``false``
Description
    Download blog avatars.


extractor.tumblr.date-min & .date-max
-------------------------------------
Type
    |Date|_
Default
    ``0`` and ``null``
Description
    Ignore all posts published before/after this date.


extractor.tumblr.external
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Follow external URLs (e.g. from "Link" posts) and try to extract
    images from them.


extractor.tumblr.inline
-----------------------
Type
    ``bool``
Default
    ``true``
Description
    Search posts for inline images and videos.


extractor.tumblr.offset
-----------------------
Type
    ``integer``
Default
    ``0``
Description
    Custom ``offset`` starting value when paginating over blog posts.

    Allows skipping over posts without having to waste API calls.


extractor.tumblr.original
-------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download full-resolution ``photo`` and ``inline`` images.

    For each photo with "maximum" resolution
    (width equal to 2048 or height equal to 3072)
    or each inline image,
    use an extra HTTP request to find the URL to its full-resolution version.


extractor.tumblr.ratelimit
--------------------------
Type
    ``string``
Default
    ``"abort"``
Description
    Selects how to handle exceeding the daily API rate limit.

    * ``"abort"``: Raise an error and stop extraction
    * ``"wait"``: Wait until rate limit reset


extractor.tumblr.reblogs
------------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    * ``true``: Extract media from reblogged posts
    * ``false``: Skip reblogged posts
    * ``"same-blog"``: Skip reblogged posts unless the original post
      is from the same blog


extractor.tumblr.posts
----------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"all"``
Example
    * ``"video,audio,link"``
    * ``["video", "audio", "link"]``
Description
    A (comma-separated) list of post types to extract images, etc. from.

    Possible types are ``text``, ``quote``, ``link``, ``answer``,
    ``video``, ``audio``, ``photo``, ``chat``.

    It is possible to use ``"all"`` instead of listing all types separately.


extractor.tumblr.fallback-delay
-------------------------------
Type
    ``float``
Default
    ``120.0``
Description
    Number of seconds to wait between retries
    for fetching full-resolution images.


extractor.tumblr.fallback-retries
---------------------------------
Type
    ``integer``
Default
    ``2``
Description
    Number of retries for fetching full-resolution images
    or ``-1`` for infinite retries.


extractor.twibooru.api-key
--------------------------
Type
    ``string``
Default
    ``null``
Description
    Your `Twibooru API Key <https://twibooru.org/users/edit>`__,
    to use your account's browsing settings and filters.


extractor.twibooru.filter
-------------------------
Type
    ``integer``
Default
    ``2`` (`Everything <https://twibooru.org/filters/2>`__ filter)
Description
    The content filter ID to use.

    Setting an explicit filter ID overrides any default filters and can be used
    to access 18+ content without `API Key <extractor.twibooru.api-key_>`__.

    See `Filters <https://twibooru.org/filters>`__ for details.


extractor.twitter.ads
---------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from promoted Tweets.


extractor.twitter.cards
-----------------------
Type
    * ``bool``
    * ``string``
Default
    ``false``
Description
    Controls how to handle `Twitter Cards <https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards>`__.

    * ``false``: Ignore cards
    * ``true``: Download image content from supported cards
    * ``"ytdl"``: Additionally download video content from unsupported cards using `youtube-dl`_


extractor.twitter.cards-blacklist
---------------------------------
Type
    ``list`` of ``strings``
Example
    ``["summary", "youtube.com", "player:twitch.tv"]``
Description
    List of card types to ignore.

    Possible values are

    * card names
    * card domains
    * ``<card name>:<card domain>``


extractor.twitter.conversations
-------------------------------
Type
    * ``bool``
    * ``string``
Default
    ``false``
Description
    For input URLs pointing to a single Tweet,
    e.g. `https://twitter.com/i/web/status/<TweetID>`,
    fetch media from all Tweets and replies in this `conversation
    <https://help.twitter.com/en/using-twitter/twitter-conversations>`__.

    If this option is equal to ``"accessible"``,
    only download from conversation Tweets
    if the given initial Tweet is accessible.


extractor.twitter.csrf
----------------------
Type
    ``string``
Default
    ``"cookies"``
Description
    Controls how to handle Cross Site Request Forgery (CSRF) tokens.

    * ``"auto"``: Always auto-generate a token.
    * ``"cookies"``: Use token given by the ``ct0`` cookie if present.


extractor.twitter.expand
------------------------
Type
    ``bool``
Default
    ``false``
Description
    For each Tweet, return *all* Tweets from that initial Tweet's
    conversation or thread, i.e. *expand* all Twitter threads.

    Going through a timeline with this option enabled is essentially the same
    as running ``gallery-dl https://twitter.com/i/web/status/<TweetID>``
    with enabled `conversations <extractor.twitter.conversations_>`__ option
    for each Tweet in said timeline.

    Note: This requires at least 1 additional API call per initial Tweet.


extractor.twitter.include
-------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"timeline"``
Example
    * ``"avatar,background,media"``
    * ``["avatar", "background", "media"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"avatar"``,
    ``"background"``,
    ``"timeline"``,
    ``"tweets"``,
    ``"media"``,
    ``"replies"``,
    ``"likes"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.twitter.transform
---------------------------
Type
    ``bool``
Default
    ``true``
Description
    Transform Tweet and User metadata into a simpler, uniform format.


extractor.twitter.tweet-endpoint
--------------------------------
Type
    ``string``
Default
    ``"auto"``
Description
    Selects the API endpoint used to retrieve single Tweets.

    * ``"restid"``: ``/TweetResultByRestId`` - accessible to guest users
    * ``"detail"``: ``/TweetDetail`` - more stable
    * ``"auto"``: ``"detail"`` when logged in, ``"restid"`` otherwise


extractor.twitter.size
----------------------
Type
    ``list`` of ``strings``
Default
    ``["orig", "4096x4096", "large", "medium", "small"]``
Description
    The image version to download.
    Any entries after the first one will be used for potential
    `fallback <extractor.*.fallback_>`_ URLs.

    Known available sizes are
    ``4096x4096``, ``orig``, ``large``, ``medium``, and ``small``.


extractor.twitter.logout
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Logout and retry as guest when access to another user's Tweets is blocked.


extractor.twitter.pinned
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from pinned Tweets.


extractor.twitter.quoted
------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from quoted Tweets.

    If this option is enabled, gallery-dl will try to fetch
    a quoted (original) Tweet when it sees the Tweet which quotes it.


extractor.twitter.ratelimit
---------------------------
Type
    ``string``
Default
    ``"wait"``
Description
    Selects how to handle exceeding the API rate limit.

    * ``"abort"``: Raise an error and stop extraction
    * ``"wait"``: Wait until rate limit reset


extractor.twitter.replies
-------------------------
Type
    ``bool``
Default
    ``true``
Description
    Fetch media from replies to other Tweets.

    If this value is ``"self"``, only consider replies where
    reply and original Tweet are from the same user.

    Note: Twitter will automatically expand conversations if you
    use the ``/with_replies`` timeline while logged in. For example,
    media from Tweets which the user replied to will also be downloaded.

    It is possible to exclude unwanted Tweets using `image-filter
    <extractor.*.image-filter_>`__.


extractor.twitter.retweets
--------------------------
Type
    ``bool``
Default
    ``false``
Description
    Fetch media from Retweets.

    If this value is ``"original"``, metadata for these files
    will be taken from the original Tweets, not the Retweets.


extractor.twitter.timeline.strategy
-----------------------------------
Type
    ``string``
Default
    ``"auto"``
Description
    Controls the strategy / tweet source used for timeline URLs
    (``https://twitter.com/USER/timeline``).

    * ``"tweets"``: `/tweets <https://twitter.com/USER/tweets>`__ timeline + search
    * ``"media"``: `/media <https://twitter.com/USER/media>`__ timeline + search
    * ``"with_replies"``: `/with_replies <https://twitter.com/USER/with_replies>`__ timeline + search
    * ``"auto"``: ``"tweets"`` or ``"media"``, depending on `retweets <extractor.twitter.retweets_>`__ and `text-tweets <extractor.twitter.text-tweets_>`__ settings


extractor.twitter.text-tweets
-----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Also emit metadata for text-only Tweets without media content.

    This only has an effect with a ``metadata`` (or ``exec``) post processor
    with `"event": "post" <metadata.event_>`_
    and appropriate `filename <metadata.filename_>`_.


extractor.twitter.twitpic
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract `TwitPic <https://twitpic.com/>`__ embeds.


extractor.twitter.unique
------------------------
Type
    ``bool``
Default
    ``true``
Description
    Ignore previously seen Tweets.


extractor.twitter.users
-----------------------
Type
    ``string``
Default
    ``"user"``
Example
    ``"https://twitter.com/search?q=from:{legacy[screen_name]}"``
Description
    | Format string for user URLs generated from
      ``following`` and ``list-members`` queries,
    | whose replacement field values come from Twitter ``user`` objects
      (`Example <https://gist.githubusercontent.com/mikf/99d2719b3845023326c7a4b6fb88dd04/raw/275b4f0541a2c7dc0a86d3998f7d253e8f10a588/github.json>`_)

    Special values:

    * ``"user"``: ``https://twitter.com/i/user/{rest_id}``
    * ``"timeline"``: ``https://twitter.com/id:{rest_id}/timeline``
    * ``"tweets"``: ``https://twitter.com/id:{rest_id}/tweets``
    * ``"media"``: ``https://twitter.com/id:{rest_id}/media``

    Note: To allow gallery-dl to follow custom URL formats, set the blacklist__
    for ``twitter`` to a non-default value, e.g. an empty string ``""``.

.. __: `extractor.*.blacklist & .whitelist`_


extractor.twitter.videos
------------------------
Type
    * ``bool``
    * ``string``
Default
    ``true``
Description
    Control video download behavior.

    * ``true``: Download videos
    * ``"ytdl"``: Download videos using `youtube-dl`_
    * ``false``: Skip video Tweets


extractor.unsplash.format
-------------------------
Type
    ``string``
Default
    ``"raw"``
Description
    Name of the image format to download.

    Available formats are
    ``"raw"``, ``"full"``, ``"regular"``, ``"small"``, and ``"thumb"``.


extractor.vsco.videos
---------------------
Type
    ``bool``
Default
    ``true``
Description
    Download video files.


extractor.wallhaven.api-key
---------------------------
Type
    ``string``
Default
    ``null``
Description
    Your `Wallhaven API Key <https://wallhaven.cc/settings/account>`__,
    to use your account's browsing settings and default filters when searching.

    See https://wallhaven.cc/help/api for more information.


extractor.wallhaven.include
---------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"uploads"``
Example
    * ``"uploads,collections"``
    * ``["uploads", "collections"]``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"uploads"``, ``"collections"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.wallhaven.metadata
----------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract additional metadata (tags, uploader)

    Note: This requires 1 additional HTTP request per post.


extractor.weasyl.api-key
------------------------
Type
    ``string``
Default
    ``null``
Description
    Your `Weasyl API Key <https://www.weasyl.com/control/apikeys>`__,
    to use your account's browsing settings and filters.


extractor.weasyl.metadata
-------------------------
Type
    ``bool``
Default
    ``false``
Description
    | Fetch extra submission metadata during gallery downloads.
    | (``comments``, ``description``, ``favorites``, ``folder_name``,
      ``tags``, ``views``)

    Note: This requires 1 additional HTTP request per submission.


extractor.weibo.include
-----------------------
Type
    * ``string``
    * ``list`` of ``strings``
Default
    ``"feed"``
Description
    A (comma-separated) list of subcategories to include
    when processing a user profile.

    Possible values are
    ``"home"``,
    ``"feed"``,
    ``"videos"``,
    ``"newvideo"``,
    ``"article"``,
    ``"album"``.

    It is possible to use ``"all"`` instead of listing all values separately.


extractor.weibo.livephoto
-------------------------
Type
    ``bool``
Default
    ``true``
Description
    Download ``livephoto`` files.


extractor.weibo.retweets
------------------------
Type
    ``bool``
Default
    ``true``
Description
    Fetch media from retweeted posts.

    If this value is ``"original"``, metadata for these files
    will be taken from the original posts, not the retweeted posts.


extractor.weibo.videos
----------------------
Type
    ``bool``
Default
    ``true``
Description
    Download video files.


extractor.ytdl.enabled
----------------------
Type
    ``bool``
Default
    ``false``
Description
    Match **all** URLs, even ones without a ``ytdl:`` prefix.


extractor.ytdl.format
---------------------
Type
    ``string``
Default
    youtube-dl's default, currently ``"bestvideo+bestaudio/best"``
Description
    Video `format selection
    <https://github.com/ytdl-org/youtube-dl#format-selection>`__
    directly passed to youtube-dl.


extractor.ytdl.generic
----------------------
Type
    ``bool``
Default
    ``true``
Description
    Controls the use of youtube-dl's generic extractor.

    Set this option to ``"force"`` for the same effect as youtube-dl's
    ``--force-generic-extractor``.


extractor.ytdl.logging
----------------------
Type
    ``bool``
Default
    ``true``
Description
    Route youtube-dl's output through gallery-dl's logging system.
    Otherwise youtube-dl will write its output directly to stdout/stderr.

    Note: Set ``quiet`` and ``no_warnings`` in
    `extractor.ytdl.raw-options`_ to ``true`` to suppress all output.


extractor.ytdl.module
---------------------
Type
    ``string``
Default
    ``null``
Description
    Name of the youtube-dl Python module to import.

    Setting this to ``null`` will try to import ``"yt_dlp"``
    followed by ``"youtube_dl"`` as fallback.


extractor.ytdl.raw-options
--------------------------
Type
    ``object`` (`name` -> `value`)
Example
    .. code:: json

        {
            "quiet": true,
            "writesubtitles": true,
            "merge_output_format": "mkv"
        }

Description
    Additional options passed directly to the ``YoutubeDL`` constructor.

    All available options can be found in `youtube-dl's docstrings
    <https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L138-L318>`__.


extractor.ytdl.cmdline-args
---------------------------
Type
    * ``string``
    * ``list`` of ``strings``
Example
    * ``"--quiet --write-sub --merge-output-format mkv"``
    * ``["--quiet", "--write-sub", "--merge-output-format", "mkv"]``
Description
    Additional options specified as youtube-dl command-line arguments.


extractor.ytdl.config-file
--------------------------
Type
    |Path|_
Example
    ``"~/.config/youtube-dl/config"``
Description
    Location of a youtube-dl configuration file to load options from.


extractor.zerochan.metadata
---------------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract additional metadata (date, md5, tags, ...)

    Note: This requires 1-2 additional HTTP requests per post.


extractor.[booru].tags
----------------------
Type
    ``bool``
Default
    ``false``
Description
    Categorize tags by their respective types
    and provide them as ``tags_<type>`` metadata fields.

    Note: This requires 1 additional HTTP request per post.


extractor.[booru].notes
-----------------------
Type
    ``bool``
Default
    ``false``
Description
    Extract overlay notes (position and text).

    Note: This requires 1 additional HTTP request per post.


extractor.[booru].url
---------------------
Type
    ``string``
Default
    ``"file_url"``
Example
    ``"preview_url"``
Description
    Alternate field name to retrieve download URLs from.


extractor.[manga-extractor].chapter-reverse
-------------------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Reverse the order of chapter URLs extracted from manga pages.

    * ``true``: Start with the latest chapter
    * ``false``: Start with the first chapter


extractor.[manga-extractor].page-reverse
----------------------------------------
Type
    ``bool``
Default
    ``false``
Description
    Download manga chapter pages in reverse order.
