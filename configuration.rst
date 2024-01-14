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
