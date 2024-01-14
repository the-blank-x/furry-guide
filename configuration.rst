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
