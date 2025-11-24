"""
Автогенерируемые TypedDict типы для Dolphin Anty API
"""
from typing import TypedDict, Optional, List, Dict, Any, Union


class pagination_metadata(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]

class proxy(TypedDict, total=False):
    """A proxy configuration object."""
    id: int
    teamId: Optional[int]
    userId: Optional[int]
    name: Optional[Any]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    port: int  # Proxy port.
    login: Optional[Any]  # Username for proxy authentication. Optional.
    password: Optional[Any]  # Password for proxy authentication. Optional.
    changeIpUrl: Optional[Any]  # URL that triggers IP rotation for the proxy. Optional. Some mobile proxy provider give the ability to rotate IP by sending a request to a special URL, and our app gives user a button to do that.
    provider: Optional[Any]  # Provider identifier if the proxy originates from a supported provider. Optional.
    ip: Optional[Any]  # Public IP address detected for this proxy (same value as `lastCheck.ip` in legacy payloads). Returned by the backend.
    savedByUser: Optional[bool]  # Indicates whether the proxy was explicitly created by the user (`true`) or auto-imported (`false`). Returned by the backend.
    browser_profiles_count: Optional[int]  # Number of browser profiles linked to this proxy (that are using this proxy).
    lastCheck: Optional[Union[Dict[str, Any], Any]]
    createdAt: Optional[str]
    updatedAt: Optional[str]

class proxy_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class proxy_create(TypedDict, total=False):
    """Parameters required to create a proxy. Most of those parameters will be given for you by your proxy provider. The connection to proxy will be established by the app on your PCs."""
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    port: int  # Proxy port.
    login: Optional[str]  # Username for proxy authentication. Optional.
    password: Optional[str]  # Password for proxy authentication. Optional.
    name: Optional[str]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    changeIpUrl: Optional[str]  # URL that triggers IP rotation for the proxy. Optional. Some mobile proxy provider give the ability to rotate IP by sending a request to a special URL, and our app gives user a button to do that.
    provider: Optional[str]  # Provider identifier if the proxy originates from a supported provider. Optional.

class SuccessResponse(TypedDict, total=False):
    success: Optional[bool]  # Indicates whether the operation was successful.

class proxy_update(TypedDict, total=False):
    """Fields identical to creation but intended for updates."""
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    port: int  # Proxy port.
    login: Optional[str]  # Username for proxy authentication. Optional.
    password: Optional[str]  # Password for proxy authentication. Optional.
    name: Optional[str]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    changeIpUrl: Optional[str]  # URL that triggers IP rotation for the proxy. Optional. Some mobile proxy provider give the ability to rotate IP by sending a request to a special URL, and our app gives user a button to do that.
    provider: Optional[str]  # Provider identifier if the proxy originates from a supported provider. Optional.

class browser_profile_status(TypedDict, total=False):
    """A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI."""
    id: int
    teamId: Optional[int]  # Team identifier that owns the status.
    userId: Optional[int]  # User identifier that created the status.
    name: str  # Human-readable name of the status. Shown in the UI near the Browser profile name.
    color: str  # Color used to render the status badge in the UI.
    deleted: Optional[int]  # 1 if the status was deleted and is kept only for historical reasons, 0 otherwise.

class browser_profile_status_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class browser_profile_status_create(TypedDict, total=False):
    """Parameters required to create a Browser profile status."""
    name: str  # Human-readable name of the status.
    color: str  # Color used to render the status badge in the UI.
    type: Optional[str]  # Status type. Currently only **common** is supported and will be used by default if omitted. Reserved for future extensions.
    profile: Optional[int]  # Identifier of a Browser profile to immediately assign this newly created status to. Optional – if omitted the status will not be applied to any profile.
    password: Optional[str]  # Password of the Browser profile given in **profile** when that profile is protected by a password. Required only if **profile** is provided and the profile has a password protection enabled.

class browser_profile_status_bulk_delete(TypedDict, total=False):
    """Delete multiple Browser profile statuses at once."""
    ids: List[int]  # Identifiers of Browser profile statuses to delete.

class browser_profile_status_update(TypedDict, total=False):
    """Fields identical to creation but intended for updates."""
    name: str  # Human-readable name of the status.
    color: str  # Color used to render the status badge in the UI.
    type: Optional[str]  # Status type. Currently only **common** is supported and will be used by default if omitted. Reserved for future extensions.
    profile: Optional[int]  # Identifier of a Browser profile to immediately assign this newly created status to. Optional – if omitted the status will not be applied to any profile.
    password: Optional[str]  # Password of the Browser profile given in **profile** when that profile is protected by a password. Required only if **profile** is provided and the profile has a password protection enabled.

class browser_profile_status_bulk_change(TypedDict, total=False):
    """Change the status for multiple Browser profiles in a single request."""
    ids: List[int]  # Identifiers of Browser profiles whose status should be changed.
    status: Dict[str, Any]  # Defines the desired status – either by referencing an existing status **id** or by providing **name** and **color** to create a new one on-the-fly.

class extension(TypedDict, total=False):
    """Extension that can be attached to Browser profiles. Extensions can either originate from the Chrome Web&nbsp;Store ("link" type) or be uploaded as a local `.zip` archive ("file" type)."""
    id: int
    teamId: Optional[int]
    userId: Optional[int]
    name: Optional[Any]  # Display name of the extension. When the extension is added from the Chrome Web&nbsp;Store it is parsed automatically from the store page. When the extension is uploaded from ZIP the name is taken from `extensionName` (or the uploaded file name if omitted).
    extensionId: Optional[Any]  # 32-character identifier of the Chrome Web&nbsp;Store extension. Empty for ZIP-uploaded extensions.
    url: str  # Link that Dolphin{anty} will use to download the CRX/ZIP. Either the Chrome Web&nbsp;Store URL of the extension or the public S3 URL of the uploaded ZIP.
    favicon: Optional[Any]  # Data URI or URL of extension icon (up to 256&nbsp;KB). Returned only when available.
    sharedToEntireTeam: bool  # If `true`, the extension is visible and can be used by every member of the team.
    mainWebsite: List[str]  # Websites where the extension is primarily used. Can help the client show contextual suggestions in the UI.
    type: Optional[str]  # How the extension was added.
    createdAt: Optional[str]
    updatedAt: Optional[str]

class extension_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class extension_create(TypedDict, total=False):
    """Parameters required to add an extension from the Chrome Web&nbsp;Store. Only **public** extensions from the store can be added &ndash; private/unpublished ones will be rejected.
"""
    url: str  # Full URL of the extension on the Chrome Web&nbsp;Store, e.g. `https://chrome.google.com/webstore/detail/adblock/gighmmpiobklfepjocnamgkkbiglidom`. The URL **must** start with one of the following prefixes:
* `https://chrome.google.com/webstore/detail/`
* `https://chromewebstore.google.com/detail/`

    sharedToEntireTeam: bool  # If `true`, the extension will become visible to every member of your team. Otherwise only you will be able to attach it to Browser profiles.

    mainWebsite: List[str]  # List of websites where the extension is mainly used. This data helps the UI to display contextual suggestions.


class extension_bulk_delete(TypedDict, total=False):
    """Identifiers of the extensions to delete."""
    ids: List[int]  # List of extension identifiers to delete.

class extension_upload(TypedDict, total=False):
    """Multipart form fields required to upload a ZIP-packed extension. Once the file is uploaded it will be stored on Dolphin{anty} S3 and a public URL will be generated automatically.
"""
    file: str  # ZIP archive containing unpacked Chrome extension (exactly what you see when you download an extension as `.crx` and then unzip it). Maximum size &ndash; **50&nbsp;MB**.

    icon: Optional[str]  # Optional custom icon that will be shown in the UI instead of taking the icon from the ZIP.
    extensionName: Optional[str]  # Optional custom display name. If omitted, the filename of the uploaded ZIP will be used.
    sharedToEntireTeam: bool  # Same meaning as in the link-based upload.
    mainWebsite: List[str]  # Websites where the extension is mainly used.

class folder(TypedDict, total=False):
    """A folder used to organise Browser profiles into groups. One folder can contain many Browser profiles and is shared within the team."""
    id: int  # Unique identifier of the folder.
    createdBy: int  # Identifier of the user who created the folder.
    teamId: int  # Identifier of the team that owns the folder.
    name: str  # Human-readable name of the folder shown in the UI.
    emoji: str  # Optional emoji icon rendered near the name to improve visual scanning.
    order: int  # Position of the folder in the user-defined sort order (higher value means higher in the list).
    isPinned: bool  # Indicates whether the folder is pinned by the current user.
    browserProfilesData: List[Dict[str, Any]]  # Quick summary information about Browser profiles contained in the folder.
    created_at: str
    updated_at: str

class folder_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class folder_create(TypedDict, total=False):
    """Parameters required to create a folder."""
    name: str  # Human-readable name of the folder.
    emoji: Optional[str]  # Optional emoji icon rendered near the name to improve visual scanning.
    isPinned: Optional[bool]  # Whether to pin the newly created folder for the current user.

class folder_update(TypedDict, total=False):
    """Fields identical to creation but intended for updates."""
    name: str  # Human-readable name of the folder.
    emoji: Optional[str]  # Optional emoji icon rendered near the name to improve visual scanning.
    isPinned: Optional[bool]  # Whether to pin the newly created folder for the current user.

class folder_order_update(TypedDict, total=False):
    """Re-ordering payload allowing to drag-and-drop folders in the UI."""
    folders: List[Dict[str, Any]]  # List of folders with their new order index (higher value ‑ higher in list).

class folder_attach_profiles(TypedDict, total=False):
    """Attach existing Browser profiles to a folder."""
    folderId: int  # Identifier of the target folder.
    profileIds: List[int]  # Identifiers of Browser profiles to attach.
    password: Optional[str]  # Optional password that will be applied to each attached profile if it was protected.

class folder_detach_profiles(TypedDict, total=False):
    """Remove Browser profiles from a folder."""
    profileIds: List[int]  # Identifiers of Browser profiles to detach from their folders.

class folder_profile_ids(TypedDict, total=False):
    """List of Browser profile identifiers contained in a folder and whether at least one of them is password-protected."""
    profileIds: List[int]  # Browser profile identifiers assigned to this folder.
    hasProfileWithPassword: bool  # Indicates whether any of the profiles in the folder is protected with a password.

class proxy_list_item(TypedDict, total=False):
    """A lightweight proxy object embedded inside the browser-profile list payload."""
    id: int
    teamId: Optional[int]
    userId: Optional[int]
    name: Optional[Any]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    changeIpUrl: Optional[bool]  # Indicates whether a change-IP endpoint is configured for this proxy.
    provider: Optional[Any]  # Provider identifier if the proxy originates from a supported provider. Optional.
    lastCheck: Optional[Union[Dict[str, Any], Any]]
    createdAt: Optional[str]
    updatedAt: Optional[str]

class browser_profile_list_item(TypedDict, total=False):
    """A complete browser profile object. A browser profile emulates a separate, fully-isolated browser instance with its own fingerprint, proxy, cookies, and other persistent data. Most write-operations that reference a browser profile will accept a subset of the fields below – this schema intentionally contains **all** attributes that can be returned by the "List browser profiles" and "Get browser profile" endpoints so that generated clients have full type-safety.
"""
    id: int
    teamId: Optional[int]  # Team identifier that owns the profile.
    userId: Optional[int]  # Identifier of the user that initially created (owns) the profile.
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Optional[Any]  # Host OS version.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Website that is indicated as the main website of the profile in the UI. Used for the profile icon, some spoof tweaks, etc.
    status: Optional[Dict[str, Any]]  # A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI.
    proxy: Optional[Dict[str, Any]]  # A lightweight proxy object embedded inside the browser-profile list payload.
    access: Optional[Dict[str, Any]]  # CRUD permissions of the current user with respect to this profile.
    pinned: Optional[bool]  # Indicates whether the profile is pinned in the UI for the current user.
    folder: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    macAddress: Optional[Union[Dict[str, Any], str, List[str]]]
    deviceName: Optional[Union[Dict[str, Any], str, List[str]]]
    audio: Optional[Union[Dict[str, Any], List[Any], str]]
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]
    totalSessionDuration: Optional[int]  # Total time (in seconds) the profile has been running since creation.
    lastStartTime: Optional[Any]  # Date & time when the profile was last started.
    created_at: Optional[str]
    updated_at: Optional[str]  # Timestamp is always returned in Europe/Moscow (UTC+03:00) timezone – the backend converts it from UTC.
    useragent: Optional[Union[Dict[str, Any], str]]
    webrtc: Optional[Union[Dict[str, Any], str]]
    canvas: Optional[Union[Dict[str, Any], str]]
    webgl: Optional[Union[Dict[str, Any], str]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Union[Dict[str, Any], str]]
    timezone: Optional[Union[Dict[str, Any], str]]
    locale: Optional[Union[Dict[str, Any], str]]
    geolocation: Optional[Union[Dict[str, Any], str]]
    cpu: Optional[Union[Dict[str, Any], int]]
    memory: Optional[Union[Dict[str, Any], int]]
    connection: Optional[Dict[str, Any]]
    ports: Optional[Union[List[int], str]]
    storagePath: Optional[str]  # Internal path for browser profile data.
    transferStatus: Optional[Any]  # When the profile is being transferred to another team this field shows the transfer status.
    transferToEmail: Optional[Any]  # Email address of the receiver when the profile transfer is in progress.
    transferHandleDate: Optional[Any]  # Date & time when the transfer request was handled (accepted or cancelled).
    transferWithProxy: Optional[Any]  # Indicates whether the proxy was moved together with the profile during transfer.
    requirePassword: Optional[bool]  # Indicates whether the profile is protected by a password (any modifying request must provide the password).
    recoverCount: Optional[int]  # Number of recovery snapshots available for the profile.
    cloudSyncDisabled: Optional[Any]  # When true, cloud sync is disabled for the profile on the current team account.
    cloudSyncDisabledOnMachineId: Optional[Any]  # Identifier of the machine that disabled cloud sync (if any).
    notes: Optional[Union[Dict[str, Any], str, Any]]

class browser_profile_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class proxy_create_or_existing(TypedDict, total=False):
    pass

class browser_profile_create(TypedDict, total=False):
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    tabs: Optional[List[str]]  # Array of URLs to open on the first launch of the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Any  # Host OS version. Fetch from the fingerprint API.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Main website associated with the profile. Affects profile icon and certain spoofing tweaks.
    statusId: Optional[Any]  # Identifier of the status to set for the profile. You can automatically set the status of a profile by attaching the status id to the profile.
    proxy: Optional[Union[Any, Any]]
    args: Optional[List[Any]]  # Custom launch arguments used by the internal browser.
    notes: Optional[List[Dict[str, Any]]]  # Arbitrary notes attached to the profile; each note is a free-form object.
    login: Optional[Any]  # Login for proxy authentication. Required if `password` is supplied.
    password: Optional[Any]  # Password for proxy authentication. Required if `login` is supplied.
    fingerprint: Optional[Dict[str, Any]]  # Raw fingerprint block returned by the fingerprint API. When present the backend derives flattened fields automatically.
    uaFullVersion: Optional[Any]  # Chrome full version string associated with the fingerprint.
    folderId: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    folder: Optional[Any]  # Deprecated – use `folderId`.
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    newHomepages: Optional[List[Dict[str, Any]]]  # Homepages to create and attach in one call (advanced). Each item mirrors the Homepage entity fields.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    fonts: Optional[List[str]]  # Custom fonts (returned only when `fontsMode` is `manual`).
    macAddress: Optional[Dict[str, Any]]  # MAC-address spoofing settings.
    deviceName: Optional[Dict[str, Any]]  # Device-name spoofing settings.
    audio: Optional[Dict[str, Any]]  # Audio fingerprint settings.
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]  # Report `navigator.doNotTrack = 1`. Take it from the fingerprint object if you do not understand what to put here.
    useragent: Optional[Dict[str, Any]]  # User-Agent spoofing settings.
    webrtc: Optional[Dict[str, Any]]
    canvas: Optional[Dict[str, Any]]
    webgl: Optional[Dict[str, Any]]
    webgpu: Optional[Dict[str, Any]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Dict[str, Any]]
    timezone: Optional[Dict[str, Any]]
    locale: Optional[Dict[str, Any]]
    geolocation: Optional[Dict[str, Any]]
    cpu: Optional[Dict[str, Any]]
    memory: Optional[Dict[str, Any]]
    screen: Optional[Dict[str, Any]]
    connectionDownlink: Optional[Any]  # Reported downlink speed in Mbps.
    connectionEffectiveType: Optional[Any]  # Reported connection type (`4g`, `3g`, …).
    connectionRtt: Optional[Any]  # Reported round-trip time in ms.
    connectionSaveData: Optional[Union[int, Any]]
    platformName: Optional[Any]  # Full platform name reported by the browser fingerprint.
    cpuArchitecture: Optional[Any]  # CPU architecture string reported by the browser fingerprint.
    osVersion: Optional[Any]  # Operating-system version string derived from the fingerprint.
    screenWidth: Optional[Any]  # Reported screen width in pixels (flattened from the screen block).
    screenHeight: Optional[Any]  # Reported screen height in pixels (flattened from the screen block).
    vendorSub: Optional[Any]  # Value of navigator.vendorSub reported by the profile.
    productSub: Optional[Any]  # Value of navigator.productSub reported by the profile.
    vendor: Optional[Any]  # Value of navigator.vendor reported by the profile.
    product: Optional[Any]  # Value of navigator.product reported by the profile.
    appCodeName: Optional[Any]  # Value of navigator.appCodeName reported by the profile.
    mediaDevices: Optional[Any]  # List of media devices returned by navigator.mediaDevices.enumerateDevices().
    userFields: Optional[List[Dict[str, Any]]]  # Arbitrary custom fields supplied by the user; each item is an object with user-defined keys.
    ports: Optional[Dict[str, Any]]  # Port protection settings for the profile.

class browser_profile_bulk_delete(TypedDict, total=False):
    ids: List[int]  # Identifiers of Browser profiles to delete.
    browserProfilePassword: Optional[str]  # Profile password. Used only when the request deletes **exactly one** profile and that profile is protected by a password. Must be omitted in all other cases.

    forceDelete: Optional[bool]  # When **true** profiles are permanently removed instead of being moved to the "Basket". Free-plan workspaces must supply this flag to confirm the intent since the basket is not available on free plans. 


class browser_profile_mass_create(TypedDict, total=False):
    items: List[Dict[str, Any]]  # Array of Browser profile definitions to create. Each element follows the same schema as a single-profile creation payload (see `BrowserProfileCreateInput`).
    common: Optional[Dict[str, Any]]

class browser_profile_transfer(TypedDict, total=False):
    ids: List[int]  # Identifiers of Browser profiles to transfer. The caller **must** be the owner of these profiles or have the `share` permission granted for them; otherwise the request will be rejected with a 403 error.

    username: str  # E-mail address of the Dolphin{anty} user who will **receive** the transferred profiles. The user may belong to the same team or to a different team/workspace. If the user is not found the request succeeds silently but no transfer is performed (this matches the backend behaviour).

    withProxy: Optional[bool]  # When `true` and a profile has a proxy attached, that proxy object **and its credentials** are moved to the receiver together with the profile. If omitted or set to `false` the profile is transferred **without** a proxy (its `proxyId` is reset to `0`).
Only proxies **owned by the sender team** can be transferred; shared or external proxies cannot be moved and will be stripped from the profile irrespective of this flag. 


class browser_profile(TypedDict, total=False):
    """A complete browser profile object. A browser profile emulates a separate, fully-isolated browser instance with its own fingerprint, proxy, cookies, and other persistent data. Most write-operations that reference a browser profile will accept a subset of the fields below – this schema intentionally contains **all** attributes that can be returned by the "List browser profiles" and "Get browser profile" endpoints so that generated clients have full type-safety.
"""
    id: int
    teamId: Optional[int]  # Team identifier that owns the profile.
    userId: Optional[int]  # Identifier of the user that initially created (owns) the profile.
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Optional[Any]  # Host OS version.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Website that is indicated as the main website of the profile in the UI. Used for the profile icon, some spoof tweaks, etc.
    status: Optional[Dict[str, Any]]  # A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI.
    proxy: Optional[Dict[str, Any]]  # A proxy configuration object.
    access: Optional[Dict[str, Any]]  # CRUD permissions of the current user with respect to this profile.
    pinned: Optional[bool]  # Indicates whether the profile is pinned in the UI for the current user.
    folder: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    fonts: Optional[List[str]]  # Custom fonts (returned only when `fontsMode` is `manual`).
    macAddress: Optional[Union[str, List[str]]]
    deviceName: Optional[Union[str, List[str]]]
    audio: Optional[Union[Dict[str, Any], List[Any], str]]
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]
    totalSessionDuration: Optional[int]  # Total time (in seconds) the profile has been running since creation.
    lastStartTime: Optional[Any]  # Date & time when the profile was last started.
    lastRunUuid: Optional[Any]  # Unique run identifier reported by the client application.
    running: Optional[bool]  # Indicates whether the profile is currently running on any user machine.
    created_at: Optional[str]
    updated_at: Optional[str]
    useragent: Optional[Union[Dict[str, Any], str]]
    webrtc: Optional[Union[Dict[str, Any], str]]
    canvas: Optional[Union[Dict[str, Any], str]]
    webgl: Optional[Union[Dict[str, Any], str]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Union[Dict[str, Any], str]]
    timezone: Optional[Union[Dict[str, Any], str]]
    locale: Optional[Union[Dict[str, Any], str]]
    geolocation: Optional[Union[Dict[str, Any], str]]
    cpu: Optional[Union[Dict[str, Any], int]]
    memory: Optional[Union[Dict[str, Any], int]]
    screen: Optional[Dict[str, Any]]
    connection: Optional[Dict[str, Any]]
    ports: Optional[Union[List[int], str]]
    storagePath: Optional[str]  # Internal path for browser profile data.
    transferStatus: Optional[Any]  # When the profile is being transferred to another team this field shows the transfer status.
    transferToEmail: Optional[Any]  # Email address of the receiver when the profile transfer is in progress.
    transferHandleDate: Optional[Any]  # Date & time when the transfer request was handled (accepted or cancelled).
    transferWithProxy: Optional[Any]  # Indicates whether the proxy was moved together with the profile during transfer.
    requirePassword: Optional[bool]  # Indicates whether the profile is protected by a password (any modifying request must provide the password).
    notes: Optional[Any]  # User-defined notes attached to the profile. Only present when the profile has non-empty notes.

class browser_profile_full(TypedDict, total=False):
    """A complete browser-profile object as returned by the "Get browser profile" endpoint.
Contains every attribute currently emitted by the backend. It **extends** the
generic `BrowserProfile` schema with additional fields such as UA version,
WebGPU, advanced device information etc.
"""
    id: int
    teamId: Optional[int]  # Team identifier that owns the profile.
    userId: Optional[int]  # Identifier of the user that initially created (owns) the profile.
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Optional[Any]  # Host OS version.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Website that is indicated as the main website of the profile in the UI. Used for the profile icon, some spoof tweaks, etc.
    status: Optional[Dict[str, Any]]  # A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI.
    proxy: Optional[Dict[str, Any]]  # A proxy configuration object.
    access: Optional[Dict[str, Any]]  # CRUD permissions of the current user with respect to this profile.
    pinned: Optional[bool]  # Indicates whether the profile is pinned in the UI for the current user.
    folder: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    homepages: Optional[List[Dict[str, Any]]]
    fontsMode: Optional[Any]
    fonts: Optional[List[str]]
    macAddress: Optional[Union[str, List[str], Dict[str, Any]]]
    deviceName: Optional[Union[str, List[str], Dict[str, Any]]]
    audio: Optional[Union[Dict[str, Any], List[Any], str]]
    isHiddenProfileName: Optional[bool]
    disableLoadWebCameraAndCookies: Optional[Any]
    enableArgIsChromeIcon: Optional[Any]
    doNotTrack: Optional[bool]
    totalSessionDuration: Optional[int]  # Total time (in seconds) the profile has been running since creation.
    lastStartTime: Optional[Any]  # Date & time when the profile was last started.
    lastRunUuid: Optional[Any]
    running: Optional[bool]  # Indicates whether the profile is currently running on any user machine.
    created_at: Optional[str]
    updated_at: Optional[str]
    useragent: Optional[Union[Dict[str, Any], str]]
    webrtc: Optional[Union[Dict[str, Any], str]]
    canvas: Optional[Union[Dict[str, Any], str]]
    webgl: Optional[Union[Dict[str, Any], str]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Union[Dict[str, Any], str]]
    timezone: Optional[Union[Dict[str, Any], str]]
    locale: Optional[Union[Dict[str, Any], str]]
    geolocation: Optional[Union[Dict[str, Any], str]]
    cpu: Optional[Union[Dict[str, Any], int]]
    memory: Optional[Union[Dict[str, Any], int]]
    screen: Optional[Dict[str, Any]]
    connection: Optional[Dict[str, Any]]
    ports: Optional[Union[List[int], str]]
    storagePath: Optional[str]
    transferStatus: Optional[Any]
    transferToEmail: Optional[Any]  # Email address of the receiver when the profile transfer is in progress.
    transferHandleDate: Optional[Any]  # Date & time when the transfer request was handled (accepted or cancelled).
    transferWithProxy: Optional[Any]  # Indicates whether the proxy was moved together with the profile during transfer.
    requirePassword: Optional[bool]  # Indicates whether the profile is protected by a password (any modifying request must provide the password).
    notes: Optional[Union[Dict[str, Any], str, Any]]
    proxyId: Optional[int]
    uaFullVersion: Optional[str]
    webgpu: Optional[Union[str, Dict[str, Any]]]
    platformName: Optional[Any]
    cpuArchitecture: Optional[Any]
    osVersion: Optional[Any]
    vendorSub: Optional[Any]
    productSub: Optional[Any]
    vendor: Optional[Any]
    product: Optional[Any]
    appCodeName: Optional[Any]
    args: Optional[List[Union[str, float, bool]]]  # Launch arguments that the desktop client will pass to the browser engine.
    tabs: Optional[List[Union[str, float, Dict[str, Any]]]]  # Opened tabs information returned only by the Get-profile endpoint.
    bookmarks: Optional[List[Dict[str, Any]]]  # Team bookmarks applicable to this profile.
    extensions: Optional[List[Dict[str, Any]]]  # Browser extensions associated with this profile.
    userFields: Optional[Dict[str, Any]]
    mediaDevices: Optional[Any]
    cloudSyncDisabled: Optional[Any]
    cloudSyncDisabledOnMachineId: Optional[Any]
    lastRunningTime: Optional[Any]
    lastRunnedByUserId: Optional[Any]
    extensionsNewNaming: Optional[bool]
    login: Optional[Any]
    password: Optional[Any]

class browser_profile_delete(TypedDict, total=False):
    browserProfilePassword: Optional[str]  # Profile password. Required only when the targeted Browser profile is protected by a password. If the profile is not password-protected this field MUST be omitted.

    forceDelete: Optional[bool]  # When **true** the profile is permanently removed instead of being moved to the "Basket". Free-plan workspaces must supply this flag to confirm the intent since the basket is not available on free plans. 


class browser_profile_update(TypedDict, total=False):
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    tabs: Optional[List[str]]  # Array of URLs to open on the first launch of the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Any  # Host OS version. Fetch from the fingerprint API.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Main website associated with the profile. Affects profile icon and certain spoofing tweaks.
    statusId: Optional[Any]  # Identifier of the status to set for the profile. You can automatically set the status of a profile by attaching the status id to the profile.
    proxy: Optional[Union[Any, Any]]
    args: Optional[List[Any]]  # Custom launch arguments used by the internal browser.
    notes: Optional[List[Dict[str, Any]]]  # Arbitrary notes attached to the profile; each note is a free-form object.
    login: Optional[Any]  # Login for proxy authentication. Required if `password` is supplied.
    password: Optional[Any]  # Password for proxy authentication. Required if `login` is supplied.
    fingerprint: Optional[Dict[str, Any]]  # Raw fingerprint block returned by the fingerprint API. When present the backend derives flattened fields automatically.
    uaFullVersion: Optional[Any]  # Chrome full version string associated with the fingerprint.
    folderId: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    folder: Optional[Any]  # Deprecated – use `folderId`.
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    newHomepages: Optional[List[Dict[str, Any]]]  # Homepages to create and attach in one call (advanced). Each item mirrors the Homepage entity fields.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    fonts: Optional[List[str]]  # Custom fonts (returned only when `fontsMode` is `manual`).
    macAddress: Optional[Dict[str, Any]]  # MAC-address spoofing settings.
    deviceName: Optional[Dict[str, Any]]  # Device-name spoofing settings.
    audio: Optional[Dict[str, Any]]  # Audio fingerprint settings.
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]  # Report `navigator.doNotTrack = 1`. Take it from the fingerprint object if you do not understand what to put here.
    useragent: Optional[Dict[str, Any]]  # User-Agent spoofing settings.
    webrtc: Optional[Dict[str, Any]]
    canvas: Optional[Dict[str, Any]]
    webgl: Optional[Dict[str, Any]]
    webgpu: Optional[Dict[str, Any]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Dict[str, Any]]
    timezone: Optional[Dict[str, Any]]
    locale: Optional[Dict[str, Any]]
    geolocation: Optional[Dict[str, Any]]
    cpu: Optional[Dict[str, Any]]
    memory: Optional[Dict[str, Any]]
    screen: Optional[Dict[str, Any]]
    connectionDownlink: Optional[Any]  # Reported downlink speed in Mbps.
    connectionEffectiveType: Optional[Any]  # Reported connection type (`4g`, `3g`, …).
    connectionRtt: Optional[Any]  # Reported round-trip time in ms.
    connectionSaveData: Optional[Union[int, Any]]
    platformName: Optional[Any]  # Full platform name reported by the browser fingerprint.
    cpuArchitecture: Optional[Any]  # CPU architecture string reported by the browser fingerprint.
    osVersion: Optional[Any]  # Operating-system version string derived from the fingerprint.
    screenWidth: Optional[Any]  # Reported screen width in pixels (flattened from the screen block).
    screenHeight: Optional[Any]  # Reported screen height in pixels (flattened from the screen block).
    vendorSub: Optional[Any]  # Value of navigator.vendorSub reported by the profile.
    productSub: Optional[Any]  # Value of navigator.productSub reported by the profile.
    vendor: Optional[Any]  # Value of navigator.vendor reported by the profile.
    product: Optional[Any]  # Value of navigator.product reported by the profile.
    appCodeName: Optional[Any]  # Value of navigator.appCodeName reported by the profile.
    mediaDevices: Optional[Any]  # List of media devices returned by navigator.mediaDevices.enumerateDevices().
    userFields: Optional[List[Dict[str, Any]]]  # Arbitrary custom fields supplied by the user; each item is an object with user-defined keys.
    ports: Optional[Dict[str, Any]]  # Port protection settings for the profile.

class browser_profile_access_multi_edit(TypedDict, total=False):
    """Input payload for **Share access to multiple browser profiles** endpoint.
Grants or revokes specific CRUD permissions for one or more users across
the selected Browser profiles in bulk.
"""
    ids: List[int]  # List of Browser profile identifiers that should be affected.
    users: List[Dict[str, Any]]  # List of user-permission descriptors. Every object configures permissions
for a single user. When `action` is `add`, the specified permission
flags are **granted** (set to `true`). When `action` is `remove`, the
same flags are **revoked** (set to `false`).

    action: str  # Specifies whether the listed permissions should be **added** (`add`) or
**removed** (`remove`). If `remove` is used, *all* supplied permission
flags must be `true` in order to fully revoke the access row.


class browser_profile_access_update(TypedDict, total=False):
    """Input payload for **Share access to browser profile** endpoint. Updates
CRUD permissions for one or more users with respect to a **single**
Browser profile.
"""
    users: List[Dict[str, Any]]  # List of user-permission descriptors. Same shape as in the bulk endpoint
but uses the `userId` key as required identifier of the target user.

    browserProfilePassword: Optional[str]  # Profile password (required only when the profile is protected with a
password). Must match the previously set password to allow permission
changes.  
Ignored when profile is not protected. 


class fingerprint(TypedDict, total=False):
    """A full browser fingerprint snapshot. This structure is returned by the
**“Get fingerprint”** endpoint and is intended to be used as-is when
creating browser profiles.

Most scalar properties are copied verbatim from real-world devices in our
internal dataset – no additional processing is applied. Keep the payload as
is to achieve maximum anti-detect quality.
"""
    screen: Dict[str, Any]  # Detailed screen metrics.
    connection: Dict[str, Any]  # Network connection metrics from the *Network Information API*.
    deviceMemory: float  # Approximate RAM size (GiB).
    hardwareConcurrency: int  # Number of logical CPU cores.
    donottrack: bool  # Reported value of the `navigator.doNotTrack` flag.
    language: str  # Primary user interface language.
    languages: str  # Comma-separated list of preferred languages.
    productSub: str  # Value of `navigator.productSub`.
    vendorSub: str  # Value of `navigator.vendorSub`.
    vendor: str  # Browser vendor.
    appCodeName: str  # Value of `navigator.appCodeName`.
    appVersion: str  # Value of `navigator.appVersion`.
    platform: str  # Host operating system reported by the browser.
    product: str  # Value of `navigator.product`.
    userAgent: str  # Full user-agent string.
    cpu: Dict[str, Any]
    os: Dict[str, Any]
    browser: Dict[str, Any]
    webgl: Dict[str, Any]
    voices: Optional[str]  # JSON-encoded list of `SpeechSynthesisVoice` objects supported by the device.
    fonts: Optional[str]  # JSON-encoded list of fonts installed on the system. Present only when the account has *Fonts override* permission.
    browserType: str  # Browser family for which the fingerprint was generated.
    platformVersion: str  # Internal Dolphin{anty} platform version identifier.
    uaFullVersion: str  # Full UA version retrieved from the *User-Agent Client Hints* API.
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` constants to their reported values. Each value is either an integer or a two-element integer array.
    webgpu: Optional[str]  # Serialized GPU adapter info captured from the *WebGPU* API.

class webgl2Maximum(TypedDict, total=False):
    """Mapping of WebGL2 `MAX_*` constants to their reported values. Each value is either an integer or a two-element integer array."""
    pass

class font(TypedDict, total=False):
    """A single font record coming from the Dolphin{anty} fingerprint dataset.  
Each entry represents a **font family** that realistically exists on the
specified platform and can therefore be safely used when overriding the
`fonts` fingerprint block.
"""
    id: int  # Unique identifier of this font record inside the dataset.
    font: str  # The full font family name (e.g. the value returned by `Canvas` API or available in CSS `font-family`).
    type: str  # Category describing how common the font is on the target platform.  

- **`default`** – ships with the operating system and is almost always present.  
- **`extra`** – frequently observed additional fonts (may be missing on a clean install).  

Treat the value as an **opaque string** – new categories may appear in the future.

    os: str  # Operating system this font belongs to.

class homepage(TypedDict, total=False):
    """Homepage record used as a custom start page in Dolphin{anty} browser profiles. Each
homepage points to a specific URL and can optionally be shared with the whole team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the homepage.
    userId: Optional[int]  # Identifier of the user who created the homepage.
    name: str  # Human-readable name shown in the UI (not the URL itself).
    url: str  # Absolute URL the browser opens on startup, including scheme (`https://`).
    sharedToEntireTeam: Optional[bool]  # When `true` the homepage becomes visible and attachable by every member of the team.
When `false` the homepage is private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories indicating where the homepage is primarily used.
This data powers contextual suggestions in the UI.

    created_at: Optional[str]
    updated_at: Optional[str]

class homepage_list_item(TypedDict, total=False):
    """Homepage record used as a custom start page in Dolphin{anty} browser profiles. Each
homepage points to a specific URL and can optionally be shared with the whole team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the homepage.
    userId: Optional[int]  # Identifier of the user who created the homepage.
    name: str  # Human-readable name shown in the UI (not the URL itself).
    url: str  # Absolute URL the browser opens on startup, including scheme (`https://`).
    sharedToEntireTeam: Optional[bool]  # When `true` the homepage becomes visible and attachable by every member of the team.
When `false` the homepage is private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories indicating where the homepage is primarily used.
This data powers contextual suggestions in the UI.

    created_at: Optional[str]
    updated_at: Optional[str]

class homepage_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class homepage_create(TypedDict, total=False):
    """Parameters required to create a homepage."""
    name: str  # Human-readable name shown in the UI.
    url: str  # Destination URL to open on browser start.
    sharedToEntireTeam: bool  # Whether to share the homepage with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this homepage.

class homepage_bulk_delete(TypedDict, total=False):
    """Delete multiple homepages at once."""
    ids: List[int]  # Identifiers of homepages to delete.

class homepage_update(TypedDict, total=False):
    """Fields identical to creation but intended for partial updates – supply only the attributes you want to change."""
    name: str  # Human-readable name shown in the UI.
    url: str  # Destination URL to open on browser start.
    sharedToEntireTeam: bool  # Whether to share the homepage with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this homepage.

class bookmark(TypedDict, total=False):
    """Bookmark record used as a custom browser bookmark (quick-access link) inside Dolphin{anty}. A bookmark always points to a particular web page and, when shared, becomes available to every member of the team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the bookmark.
    userId: Optional[int]  # Identifier of the user who created the bookmark.
    name: str  # Human-readable label shown in the Dolphin{anty} UI.
    url: str  # Absolute URL the built-in browser navigates to when the bookmark is clicked.
    favicon: Optional[Any]  # Link to the page favicon. The backend attempts to auto-fetch the icon on creation, therefore this field is usually **null** in the request payload and populated only in the response.

    sharedToEntireTeam: Optional[bool]  # When `true` the bookmark is visible and attachable by **all** team members. When `false` it stays private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories designating the environment where the bookmark is predominantly used. Accepted values are the same as for browser profiles and homepages.

Used for automatically applying the bookmark to the browser profiles with the same main website.

    created_at: Optional[str]
    updated_at: Optional[str]

class bookmark_list_item(TypedDict, total=False):
    """Bookmark record used as a custom browser bookmark (quick-access link) inside Dolphin{anty}. A bookmark always points to a particular web page and, when shared, becomes available to every member of the team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the bookmark.
    userId: Optional[int]  # Identifier of the user who created the bookmark.
    name: str  # Human-readable label shown in the Dolphin{anty} UI.
    url: str  # Absolute URL the built-in browser navigates to when the bookmark is clicked.
    favicon: Optional[Any]  # Link to the page favicon. The backend attempts to auto-fetch the icon on creation, therefore this field is usually **null** in the request payload and populated only in the response.

    sharedToEntireTeam: Optional[bool]  # When `true` the bookmark is visible and attachable by **all** team members. When `false` it stays private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories designating the environment where the bookmark is predominantly used. Accepted values are the same as for browser profiles and homepages.

Used for automatically applying the bookmark to the browser profiles with the same main website.

    created_at: Optional[str]
    updated_at: Optional[str]

class bookmark_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class bookmark_create(TypedDict, total=False):
    """Parameters required to create a bookmark."""
    name: str  # Human-readable label shown in the UI.
    url: str  # Destination URL to open when the bookmark is activated.
    sharedToEntireTeam: bool  # Whether to share the bookmark with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this bookmark.

class bookmark_bulk_delete(TypedDict, total=False):
    """Delete multiple bookmarks at once."""
    ids: List[int]  # Identifiers of bookmarks to delete.

class bookmark_update(TypedDict, total=False):
    """Fields identical to creation but intended for partial updates – supply only the attributes you want to change."""
    name: str  # Human-readable label shown in the UI.
    url: str  # Destination URL to open when the bookmark is activated.
    sharedToEntireTeam: bool  # Whether to share the bookmark with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this bookmark.

class team_user(TypedDict, total=False):
    """A team user represents a member of the current team account.
Team members share access to browser profiles, folders and other resources
according to their role and access settings described below.
"""
    id: int  # Unique identifier of the user inside Dolphin{anty}.
    teamId: Optional[int]  # Identifier of the team the user belongs to.
    username: str  # E-mail used to log into Dolphin{anty}.
    displayName: Optional[Any]  # Human-readable name shown in the UI. When null the username is used instead.
    telegram: Optional[Any]  # Telegram username linked to the account (without the `@` sign).
    role: str  # Role of the user inside the team.
• `admin` – full control over the team account
• `teamlead` – manages a subset of users and resources
• `user` – regular member with limited permissions

    teamleads: Optional[List[int]]  # List of identifiers of team-lead users supervising the member.
    access_setting: Optional[Dict[str, Any]]  # Fine-grained limits applied to the user.
    created_at: Optional[str]  # Date & time when the user was created (Europe/Moscow, UTC+03:00).
    updated_at: Optional[str]  # Date & time of the last update (Europe/Moscow, UTC+03:00).

class team_user_list_item(TypedDict, total=False):
    """A team user represents a member of the current team account.
Team members share access to browser profiles, folders and other resources
according to their role and access settings described below.
"""
    id: int  # Unique identifier of the user inside Dolphin{anty}.
    teamId: Optional[int]  # Identifier of the team the user belongs to.
    username: str  # E-mail used to log into Dolphin{anty}.
    displayName: Optional[Any]  # Human-readable name shown in the UI. When null the username is used instead.
    telegram: Optional[Any]  # Telegram username linked to the account (without the `@` sign).
    role: str  # Role of the user inside the team.
• `admin` – full control over the team account
• `teamlead` – manages a subset of users and resources
• `user` – regular member with limited permissions

    teamleads: Optional[List[int]]  # List of identifiers of team-lead users supervising the member.
    access_setting: Optional[Dict[str, Any]]  # Fine-grained limits applied to the user.
    created_at: Optional[str]  # Date & time when the user was created (Europe/Moscow, UTC+03:00).
    updated_at: Optional[str]  # Date & time of the last update (Europe/Moscow, UTC+03:00).

class team_user_list(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class team_user_create(TypedDict, total=False):
    """Payload for creating a new member inside the current team account.
Only users with the `admin` role can add team members.
"""
    username: str  # Unique e-mail address used as the login for the new user.
    password: str  # Login password for the new user.
Must be 8–512 characters long.

    role: str  # Role to assign to the new user.
    displayName: Optional[str]  # Human-readable name shown in the UI.
    teamleads: Optional[List[int]]  # Identifiers of team-lead users supervising the member.
Can only be provided when `role` is `user`.

    canCreateBp: Optional[bool]  # Grants the permission to create new browser profiles.
When omitted the permission defaults to the backend logic depending on the requester role.

    unlimitedBp: Optional[bool]  # When `true` the user is not limited by `bpLimit`.
Must be provided **together** with `canCreateBp=true`.

    bpLimit: Optional[int]  # Hard limit for the amount of browser profiles the user can own.
Ignored when `unlimitedBp` is set to `true`. 


class team_user_update(TypedDict, total=False):
    """Set of fields that can be modified for an existing team user. 
All properties are optional – provide only those you need to change.
"""
    password: Optional[str]  # New login password. When omitted the password is not changed.
    username: Optional[str]  # New login e-mail. Must be unique within Dolphin{anty}.
    displayName: Optional[str]  # New human-readable name shown in the UI.
    role: Optional[str]  # New role to assign to the user.
    teamleads: Optional[List[int]]  # Identifiers of team-lead users supervising the member. Passing an empty array removes supervisors.
    canCreateBp: Optional[bool]  # Grant or revoke the permission to create browser profiles.
    unlimitedBp: Optional[bool]  # When `true` the user is not limited by `bpLimit`.
Must be provided **together** with `canCreateBp=true`.

    bpLimit: Optional[int]  # Hard limit for the amount of browser profiles the user can own.
Ignored when `unlimitedBp` is set to `true`. 


class local_storage_item(TypedDict, total=False):
    """Single Local Storage snapshot for one origin. When exporting Local Storage the backend
groups key/value pairs by their associated **domain** (origin). Each object therefore
contains data for exactly one domain.
"""
    domain: str  # Origin (domain) the Local Storage belongs to. A special placeholder value
`dolphin-anty-export` is used by the backend when the export represents a
flattened dump that mixes keys from multiple origins.

    data: Dict[str, Any]  # Dictionary of Local Storage entries as they are kept inside Chromium’s
LevelDB. **Both keys and values are Base-64 encoded strings**. Consumers
normally treat this object as an opaque blob – you rarely need to decode
it manually.


class local_storage_export(TypedDict, total=False):
    """Complete Local Storage dump produced by the export endpoints. The array
contains one or more `LocalStorageItem` objects – one per origin.
"""
    pass

class local_storage_import(TypedDict, total=False):
    """Payload accepted by `POST /local-storage/import`.
"""
    profileId: int  # Identifier of the browser profile that should receive the Local Storage.
    localStorage: List[Dict[str, Any]]  # Complete Local Storage dump produced by the export endpoints. The array
contains one or more `LocalStorageItem` objects – one per origin.

    transfer: Union[int, bool]
    plan: str  # Subscription plan of the caller.

    browserProfilePassword: Optional[Any]  # Password protecting the target profile (if `requirePassword` is enabled).
Omit or pass `null` when not used.

    cloudSyncDisabled: Optional[bool]  # When `true` skips downloading the existing datadir from cloud storage and does not
push the archive back after import.


class cookie_item(TypedDict, total=False):
    """Single browser cookie entry as stored in Chromium’s SQLite `Cookies` DB. Each
object represents **one** cookie (name/value pair).
"""
    domain: str  # Hostname the cookie applies to (leading dot allowed for subdomains).
    name: str  # Cookie name.
    value: str  # Raw cookie value.
    path: str  # Resource path scope.
    expirationDate: int  # Expiration timestamp in **milliseconds** since Unix epoch (Chromium format).

    secure: Optional[bool]  # When `true`, the cookie is only sent over HTTPS.
    httpOnly: Optional[bool]  # When `true`, the cookie is inaccessible to JavaScript (`document.cookie`).

    sameSite: Optional[str]  # SameSite attribute controlling cross-site behaviour.

class cookies_export(TypedDict, total=False):
    """Flat list of cookies produced by the export endpoints. The array contains
zero or more `CookieItem` objects.
"""
    pass

class cookies_import(TypedDict, total=False):
    """Payload accepted by `POST /cookies/import`.
"""
    profileId: int  # Identifier of the browser profile that will receive the cookies.
    cookies: List[Dict[str, Any]]  # Flat list of cookies produced by the export endpoints. The array contains
zero or more `CookieItem` objects.

    transfer: Union[int, bool]
    browserProfilePassword: Optional[Any]  # Password protecting the target profile (if `requirePassword` is enabled).
Omit or pass `null` when not used.

    cloudSyncDisabled: Optional[bool]  # When `true` skips downloading the existing datadir from cloud storage and
does not push the archive back after import.


class cookies_export_input(TypedDict, total=False):
    """Payload accepted by `POST /export-cookies`.
"""
    browserProfiles: List[Dict[str, Any]]  # Array describing the profiles to export cookies from. Each element must
contain at least the profile `id` and `name`.

    plan: Optional[str]  # Subscription plan of the caller.
    doNotSave: Optional[bool]  # When `true`, the backend does **not** write `.txt` files to the host’s
*Downloads* folder. The cookie data is still returned in the response.


class cookies_export_response(TypedDict, total=False):
    """Successful cookies export payload."""
    success: bool
    cookies: List[Dict[str, Any]]  # Flat list of cookies produced by the export endpoints. The array contains
zero or more `CookieItem` objects.


class cookie_robot_start(TypedDict, total=False):
    """Payload accepted by `POST /cookies/{browserProfileId}/robot`.
Instructs Dolphin{anty} to visit every supplied URL in an invisible browser
page and persist the cookies produced by the websites into the specified
browser profile.
"""
    data: List[str]  # One or more absolute URLs (including the `http`/`https` scheme) that the
robot must open **sequentially**. After each page finishes loading (the
network is idle) the backend waits a couple of seconds for late async
requests, then extracts all cookies, closes the tab and proceeds to the
next URL.

    headless: bool  # When `true` the Anty browser is launched in **headless** mode (no GUI). In
this mode the robot consumes less resources and works on machines without
a window manager. Internally this flag also disables opening profile tabs
to speed up startup.

    imageless: bool  # When `true` the Chromium network stack skips downloading images. This
significantly speeds up crawling heavy pages when only cookies are
required.

    plan: Optional[Any]  # *(Optional)* Reserved debugging field. The value is ignored and replaced
by the authenticated account’s actual plan on the backend. Pass `null` or
omit entirely.

    browserProfilePassword: Optional[Any]  # Password protecting the target profile (needed when the profile was
created with `requirePassword = true`). Provide the plaintext password so
the robot can decrypt and write the *Cookies* SQLite database. Omit or
pass `null` when the profile is not locked.


class browser_profile_start(TypedDict, total=False):
    """Payload accepted by `POST /browser_profiles/{browserProfileId}/start`.
Controls how the local Anty browser instance is launched. All fields are
optional – when omitted the backend falls back to the defaults used by the
Desktop application.
"""
    screenWidth: Optional[int]  # Logical width of the your real screen. Used as a fallback for the screen width if you use "screen" spoof in `real` mode.
    screenHeight: Optional[int]  # Logical height of the your real screen. Used as a fallback for the screen height if you use "screen" spoof in `real` mode.
    dpr: Optional[float]  # Device-pixel ratio of your real screen. On Windows the backend internally
multiplies `screenWidth`/`screenHeight` by this factor to emulate HiDPI
(retina) displays. On macOS this will likely be 2, and on Windows it will depend on the display settings. Used only if you use "screen" spoof in `real` mode.

    headless: Optional[bool]  # When `true` the browser is launched in Chromium **headless** mode (no
GUI). This flag implicitly sets `noTabs = true`.

    automation: Optional[bool]  # Enables remote automation APIs (Puppeteer / Playwright / Selenium). When set to
`true` the successful response contains the `automation` object with the
connection details (`port`, `wsEndpoint`).

This feature is **unavailable on the Free plan** – the backend returns
**HTTP 402** when requested.

    noTabs: Optional[bool]  # Skips restoring the profile tabs after launch and leaves the instance
completely blank. Automatically forced to `true` when both `headless`
and `automation` are enabled.

    is_owned: Optional[bool]  # Marks the current machine as the **owner** of the running Synchronizer session – this makes other browsers copy any actions you do in this browser.

    name_session: Optional[str]  # Any identifier, e.g. UUIDv4, used to identify the running synchronizer session. All profiles in the same session will mirror the actions of **Owned** profile.
    plan: Optional[Any]  # Your current subscription plan.

    transfer: Optional[Any]  # *(Internal)* Starts the browser in **transfer** mode, which means the profile is currently is in transfer between teams. Normal clients should omit the field.

    browserProfilePassword: Optional[Any]  # Plain-text password protecting the target profile. Required only when the
profile was created with specific password set.


class login_with_token(TypedDict, total=False):
    """Payload accepted by `POST /login-with-token`. Stores a
remote Dolphin{anty} **JWT token** inside the Local API and optionally applies
pre-fetched feature flags for the current machine.
"""
    token: str  # The **exact** JWT bearer token generated in the web panel
(https://dolphin-anty.com/panel). The value is stored locally (encrypted
if the OS keychain is available) and will be attached to all subsequent
requests sent by the Local API to the remote Dolphin{anty} endpoints.


class Proxy(TypedDict, total=False):
    """A proxy configuration object."""
    id: int
    teamId: Optional[int]
    userId: Optional[int]
    name: Optional[Any]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    port: int  # Proxy port.
    login: Optional[Any]  # Username for proxy authentication. Optional.
    password: Optional[Any]  # Password for proxy authentication. Optional.
    changeIpUrl: Optional[Any]  # URL that triggers IP rotation for the proxy. Optional. Some mobile proxy provider give the ability to rotate IP by sending a request to a special URL, and our app gives user a button to do that.
    provider: Optional[Any]  # Provider identifier if the proxy originates from a supported provider. Optional.
    ip: Optional[Any]  # Public IP address detected for this proxy (same value as `lastCheck.ip` in legacy payloads). Returned by the backend.
    savedByUser: Optional[bool]  # Indicates whether the proxy was explicitly created by the user (`true`) or auto-imported (`false`). Returned by the backend.
    browser_profiles_count: Optional[int]  # Number of browser profiles linked to this proxy (that are using this proxy).
    lastCheck: Optional[Union[Dict[str, Any], Any]]
    createdAt: Optional[str]
    updatedAt: Optional[str]

class ProxyCreateOrExisting(TypedDict, total=False):
    pass

class ProxyCreateInput(TypedDict, total=False):
    """Parameters required to create a proxy. Most of those parameters will be given for you by your proxy provider. The connection to proxy will be established by the app on your PCs."""
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    port: int  # Proxy port.
    login: Optional[str]  # Username for proxy authentication. Optional.
    password: Optional[str]  # Password for proxy authentication. Optional.
    name: Optional[str]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    changeIpUrl: Optional[str]  # URL that triggers IP rotation for the proxy. Optional. Some mobile proxy provider give the ability to rotate IP by sending a request to a special URL, and our app gives user a button to do that.
    provider: Optional[str]  # Provider identifier if the proxy originates from a supported provider. Optional.

class ProxyUpdateInput(TypedDict, total=False):
    """Fields identical to creation but intended for updates."""
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    port: int  # Proxy port.
    login: Optional[str]  # Username for proxy authentication. Optional.
    password: Optional[str]  # Password for proxy authentication. Optional.
    name: Optional[str]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    changeIpUrl: Optional[str]  # URL that triggers IP rotation for the proxy. Optional. Some mobile proxy provider give the ability to rotate IP by sending a request to a special URL, and our app gives user a button to do that.
    provider: Optional[str]  # Provider identifier if the proxy originates from a supported provider. Optional.

class ProxyList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class ProxyListItem(TypedDict, total=False):
    """A lightweight proxy object embedded inside the browser-profile list payload."""
    id: int
    teamId: Optional[int]
    userId: Optional[int]
    name: Optional[Any]  # Human-readable alias for the proxy. Optional. Used in the UI to fastly recognize or search for the proxy. If skipped, the proxy will be named after it is host, port, login (if provided) and password (if provided), i.e. `protocol://login:password@host:port`.
    type: str  # Proxy protocol type.
    host: str  # Proxy URL or IPv4/IPv6 address.
    changeIpUrl: Optional[bool]  # Indicates whether a change-IP endpoint is configured for this proxy.
    provider: Optional[Any]  # Provider identifier if the proxy originates from a supported provider. Optional.
    lastCheck: Optional[Union[Dict[str, Any], Any]]
    createdAt: Optional[str]
    updatedAt: Optional[str]

class PaginationMetadata(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]

class BrowserProfileStatus(TypedDict, total=False):
    """A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI."""
    id: int
    teamId: Optional[int]  # Team identifier that owns the status.
    userId: Optional[int]  # User identifier that created the status.
    name: str  # Human-readable name of the status. Shown in the UI near the Browser profile name.
    color: str  # Color used to render the status badge in the UI.
    deleted: Optional[int]  # 1 if the status was deleted and is kept only for historical reasons, 0 otherwise.

class BrowserProfileStatusCreateInput(TypedDict, total=False):
    """Parameters required to create a Browser profile status."""
    name: str  # Human-readable name of the status.
    color: str  # Color used to render the status badge in the UI.
    type: Optional[str]  # Status type. Currently only **common** is supported and will be used by default if omitted. Reserved for future extensions.
    profile: Optional[int]  # Identifier of a Browser profile to immediately assign this newly created status to. Optional – if omitted the status will not be applied to any profile.
    password: Optional[str]  # Password of the Browser profile given in **profile** when that profile is protected by a password. Required only if **profile** is provided and the profile has a password protection enabled.

class BrowserProfileStatusUpdateInput(TypedDict, total=False):
    """Fields identical to creation but intended for updates."""
    name: str  # Human-readable name of the status.
    color: str  # Color used to render the status badge in the UI.
    type: Optional[str]  # Status type. Currently only **common** is supported and will be used by default if omitted. Reserved for future extensions.
    profile: Optional[int]  # Identifier of a Browser profile to immediately assign this newly created status to. Optional – if omitted the status will not be applied to any profile.
    password: Optional[str]  # Password of the Browser profile given in **profile** when that profile is protected by a password. Required only if **profile** is provided and the profile has a password protection enabled.

class BrowserProfileStatusList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class BrowserProfileStatusBulkChangeInput(TypedDict, total=False):
    """Change the status for multiple Browser profiles in a single request."""
    ids: List[int]  # Identifiers of Browser profiles whose status should be changed.
    status: Dict[str, Any]  # Defines the desired status – either by referencing an existing status **id** or by providing **name** and **color** to create a new one on-the-fly.

class BrowserProfileStatusBulkDeleteInput(TypedDict, total=False):
    """Delete multiple Browser profile statuses at once."""
    ids: List[int]  # Identifiers of Browser profile statuses to delete.

class Extension(TypedDict, total=False):
    """Extension that can be attached to Browser profiles. Extensions can either originate from the Chrome Web&nbsp;Store ("link" type) or be uploaded as a local `.zip` archive ("file" type)."""
    id: int
    teamId: Optional[int]
    userId: Optional[int]
    name: Optional[Any]  # Display name of the extension. When the extension is added from the Chrome Web&nbsp;Store it is parsed automatically from the store page. When the extension is uploaded from ZIP the name is taken from `extensionName` (or the uploaded file name if omitted).
    extensionId: Optional[Any]  # 32-character identifier of the Chrome Web&nbsp;Store extension. Empty for ZIP-uploaded extensions.
    url: str  # Link that Dolphin{anty} will use to download the CRX/ZIP. Either the Chrome Web&nbsp;Store URL of the extension or the public S3 URL of the uploaded ZIP.
    favicon: Optional[Any]  # Data URI or URL of extension icon (up to 256&nbsp;KB). Returned only when available.
    sharedToEntireTeam: bool  # If `true`, the extension is visible and can be used by every member of the team.
    mainWebsite: List[str]  # Websites where the extension is primarily used. Can help the client show contextual suggestions in the UI.
    type: Optional[str]  # How the extension was added.
    createdAt: Optional[str]
    updatedAt: Optional[str]

class ExtensionCreateInput(TypedDict, total=False):
    """Parameters required to add an extension from the Chrome Web&nbsp;Store. Only **public** extensions from the store can be added &ndash; private/unpublished ones will be rejected.
"""
    url: str  # Full URL of the extension on the Chrome Web&nbsp;Store, e.g. `https://chrome.google.com/webstore/detail/adblock/gighmmpiobklfepjocnamgkkbiglidom`. The URL **must** start with one of the following prefixes:
* `https://chrome.google.com/webstore/detail/`
* `https://chromewebstore.google.com/detail/`

    sharedToEntireTeam: bool  # If `true`, the extension will become visible to every member of your team. Otherwise only you will be able to attach it to Browser profiles.

    mainWebsite: List[str]  # List of websites where the extension is mainly used. This data helps the UI to display contextual suggestions.


class ExtensionUploadInput(TypedDict, total=False):
    """Multipart form fields required to upload a ZIP-packed extension. Once the file is uploaded it will be stored on Dolphin{anty} S3 and a public URL will be generated automatically.
"""
    file: str  # ZIP archive containing unpacked Chrome extension (exactly what you see when you download an extension as `.crx` and then unzip it). Maximum size &ndash; **50&nbsp;MB**.

    icon: Optional[str]  # Optional custom icon that will be shown in the UI instead of taking the icon from the ZIP.
    extensionName: Optional[str]  # Optional custom display name. If omitted, the filename of the uploaded ZIP will be used.
    sharedToEntireTeam: bool  # Same meaning as in the link-based upload.
    mainWebsite: List[str]  # Websites where the extension is mainly used.

class ExtensionList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class ExtensionBulkDeleteInput(TypedDict, total=False):
    """Identifiers of the extensions to delete."""
    ids: List[int]  # List of extension identifiers to delete.

class Folder(TypedDict, total=False):
    """A folder used to organise Browser profiles into groups. One folder can contain many Browser profiles and is shared within the team."""
    id: int  # Unique identifier of the folder.
    createdBy: int  # Identifier of the user who created the folder.
    teamId: int  # Identifier of the team that owns the folder.
    name: str  # Human-readable name of the folder shown in the UI.
    emoji: str  # Optional emoji icon rendered near the name to improve visual scanning.
    order: int  # Position of the folder in the user-defined sort order (higher value means higher in the list).
    isPinned: bool  # Indicates whether the folder is pinned by the current user.
    browserProfilesData: List[Dict[str, Any]]  # Quick summary information about Browser profiles contained in the folder.
    created_at: str
    updated_at: str

class FolderCreateInput(TypedDict, total=False):
    """Parameters required to create a folder."""
    name: str  # Human-readable name of the folder.
    emoji: Optional[str]  # Optional emoji icon rendered near the name to improve visual scanning.
    isPinned: Optional[bool]  # Whether to pin the newly created folder for the current user.

class FolderUpdateInput(TypedDict, total=False):
    """Fields identical to creation but intended for updates."""
    name: str  # Human-readable name of the folder.
    emoji: Optional[str]  # Optional emoji icon rendered near the name to improve visual scanning.
    isPinned: Optional[bool]  # Whether to pin the newly created folder for the current user.

class FolderList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class FolderOrderUpdateInput(TypedDict, total=False):
    """Re-ordering payload allowing to drag-and-drop folders in the UI."""
    folders: List[Dict[str, Any]]  # List of folders with their new order index (higher value ‑ higher in list).

class FolderAttachProfilesInput(TypedDict, total=False):
    """Attach existing Browser profiles to a folder."""
    folderId: int  # Identifier of the target folder.
    profileIds: List[int]  # Identifiers of Browser profiles to attach.
    password: Optional[str]  # Optional password that will be applied to each attached profile if it was protected.

class FolderDetachProfilesInput(TypedDict, total=False):
    """Remove Browser profiles from a folder."""
    profileIds: List[int]  # Identifiers of Browser profiles to detach from their folders.

class FolderProfileIds(TypedDict, total=False):
    """List of Browser profile identifiers contained in a folder and whether at least one of them is password-protected."""
    profileIds: List[int]  # Browser profile identifiers assigned to this folder.
    hasProfileWithPassword: bool  # Indicates whether any of the profiles in the folder is protected with a password.

class BrowserProfile(TypedDict, total=False):
    """A complete browser profile object. A browser profile emulates a separate, fully-isolated browser instance with its own fingerprint, proxy, cookies, and other persistent data. Most write-operations that reference a browser profile will accept a subset of the fields below – this schema intentionally contains **all** attributes that can be returned by the "List browser profiles" and "Get browser profile" endpoints so that generated clients have full type-safety.
"""
    id: int
    teamId: Optional[int]  # Team identifier that owns the profile.
    userId: Optional[int]  # Identifier of the user that initially created (owns) the profile.
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Optional[Any]  # Host OS version.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Website that is indicated as the main website of the profile in the UI. Used for the profile icon, some spoof tweaks, etc.
    status: Optional[Dict[str, Any]]  # A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI.
    proxy: Optional[Dict[str, Any]]  # A proxy configuration object.
    access: Optional[Dict[str, Any]]  # CRUD permissions of the current user with respect to this profile.
    pinned: Optional[bool]  # Indicates whether the profile is pinned in the UI for the current user.
    folder: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    fonts: Optional[List[str]]  # Custom fonts (returned only when `fontsMode` is `manual`).
    macAddress: Optional[Union[str, List[str]]]
    deviceName: Optional[Union[str, List[str]]]
    audio: Optional[Union[Dict[str, Any], List[Any], str]]
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]
    totalSessionDuration: Optional[int]  # Total time (in seconds) the profile has been running since creation.
    lastStartTime: Optional[Any]  # Date & time when the profile was last started.
    lastRunUuid: Optional[Any]  # Unique run identifier reported by the client application.
    running: Optional[bool]  # Indicates whether the profile is currently running on any user machine.
    created_at: Optional[str]
    updated_at: Optional[str]
    useragent: Optional[Union[Dict[str, Any], str]]
    webrtc: Optional[Union[Dict[str, Any], str]]
    canvas: Optional[Union[Dict[str, Any], str]]
    webgl: Optional[Union[Dict[str, Any], str]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Union[Dict[str, Any], str]]
    timezone: Optional[Union[Dict[str, Any], str]]
    locale: Optional[Union[Dict[str, Any], str]]
    geolocation: Optional[Union[Dict[str, Any], str]]
    cpu: Optional[Union[Dict[str, Any], int]]
    memory: Optional[Union[Dict[str, Any], int]]
    screen: Optional[Dict[str, Any]]
    connection: Optional[Dict[str, Any]]
    ports: Optional[Union[List[int], str]]
    storagePath: Optional[str]  # Internal path for browser profile data.
    transferStatus: Optional[Any]  # When the profile is being transferred to another team this field shows the transfer status.
    transferToEmail: Optional[Any]  # Email address of the receiver when the profile transfer is in progress.
    transferHandleDate: Optional[Any]  # Date & time when the transfer request was handled (accepted or cancelled).
    transferWithProxy: Optional[Any]  # Indicates whether the proxy was moved together with the profile during transfer.
    requirePassword: Optional[bool]  # Indicates whether the profile is protected by a password (any modifying request must provide the password).
    notes: Optional[Any]  # User-defined notes attached to the profile. Only present when the profile has non-empty notes.

class BrowserProfileCreateInput(TypedDict, total=False):
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    tabs: Optional[List[str]]  # Array of URLs to open on the first launch of the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Any  # Host OS version. Fetch from the fingerprint API.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Main website associated with the profile. Affects profile icon and certain spoofing tweaks.
    statusId: Optional[Any]  # Identifier of the status to set for the profile. You can automatically set the status of a profile by attaching the status id to the profile.
    proxy: Optional[Union[Any, Any]]
    args: Optional[List[Any]]  # Custom launch arguments used by the internal browser.
    notes: Optional[List[Dict[str, Any]]]  # Arbitrary notes attached to the profile; each note is a free-form object.
    login: Optional[Any]  # Login for proxy authentication. Required if `password` is supplied.
    password: Optional[Any]  # Password for proxy authentication. Required if `login` is supplied.
    fingerprint: Optional[Dict[str, Any]]  # Raw fingerprint block returned by the fingerprint API. When present the backend derives flattened fields automatically.
    uaFullVersion: Optional[Any]  # Chrome full version string associated with the fingerprint.
    folderId: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    folder: Optional[Any]  # Deprecated – use `folderId`.
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    newHomepages: Optional[List[Dict[str, Any]]]  # Homepages to create and attach in one call (advanced). Each item mirrors the Homepage entity fields.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    fonts: Optional[List[str]]  # Custom fonts (returned only when `fontsMode` is `manual`).
    macAddress: Optional[Dict[str, Any]]  # MAC-address spoofing settings.
    deviceName: Optional[Dict[str, Any]]  # Device-name spoofing settings.
    audio: Optional[Dict[str, Any]]  # Audio fingerprint settings.
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]  # Report `navigator.doNotTrack = 1`. Take it from the fingerprint object if you do not understand what to put here.
    useragent: Optional[Dict[str, Any]]  # User-Agent spoofing settings.
    webrtc: Optional[Dict[str, Any]]
    canvas: Optional[Dict[str, Any]]
    webgl: Optional[Dict[str, Any]]
    webgpu: Optional[Dict[str, Any]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Dict[str, Any]]
    timezone: Optional[Dict[str, Any]]
    locale: Optional[Dict[str, Any]]
    geolocation: Optional[Dict[str, Any]]
    cpu: Optional[Dict[str, Any]]
    memory: Optional[Dict[str, Any]]
    screen: Optional[Dict[str, Any]]
    connectionDownlink: Optional[Any]  # Reported downlink speed in Mbps.
    connectionEffectiveType: Optional[Any]  # Reported connection type (`4g`, `3g`, …).
    connectionRtt: Optional[Any]  # Reported round-trip time in ms.
    connectionSaveData: Optional[Union[int, Any]]
    platformName: Optional[Any]  # Full platform name reported by the browser fingerprint.
    cpuArchitecture: Optional[Any]  # CPU architecture string reported by the browser fingerprint.
    osVersion: Optional[Any]  # Operating-system version string derived from the fingerprint.
    screenWidth: Optional[Any]  # Reported screen width in pixels (flattened from the screen block).
    screenHeight: Optional[Any]  # Reported screen height in pixels (flattened from the screen block).
    vendorSub: Optional[Any]  # Value of navigator.vendorSub reported by the profile.
    productSub: Optional[Any]  # Value of navigator.productSub reported by the profile.
    vendor: Optional[Any]  # Value of navigator.vendor reported by the profile.
    product: Optional[Any]  # Value of navigator.product reported by the profile.
    appCodeName: Optional[Any]  # Value of navigator.appCodeName reported by the profile.
    mediaDevices: Optional[Any]  # List of media devices returned by navigator.mediaDevices.enumerateDevices().
    userFields: Optional[List[Dict[str, Any]]]  # Arbitrary custom fields supplied by the user; each item is an object with user-defined keys.
    ports: Optional[Dict[str, Any]]  # Port protection settings for the profile.

class BrowserProfileUpdateInput(TypedDict, total=False):
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    tabs: Optional[List[str]]  # Array of URLs to open on the first launch of the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Any  # Host OS version. Fetch from the fingerprint API.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Main website associated with the profile. Affects profile icon and certain spoofing tweaks.
    statusId: Optional[Any]  # Identifier of the status to set for the profile. You can automatically set the status of a profile by attaching the status id to the profile.
    proxy: Optional[Union[Any, Any]]
    args: Optional[List[Any]]  # Custom launch arguments used by the internal browser.
    notes: Optional[List[Dict[str, Any]]]  # Arbitrary notes attached to the profile; each note is a free-form object.
    login: Optional[Any]  # Login for proxy authentication. Required if `password` is supplied.
    password: Optional[Any]  # Password for proxy authentication. Required if `login` is supplied.
    fingerprint: Optional[Dict[str, Any]]  # Raw fingerprint block returned by the fingerprint API. When present the backend derives flattened fields automatically.
    uaFullVersion: Optional[Any]  # Chrome full version string associated with the fingerprint.
    folderId: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    folder: Optional[Any]  # Deprecated – use `folderId`.
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    newHomepages: Optional[List[Dict[str, Any]]]  # Homepages to create and attach in one call (advanced). Each item mirrors the Homepage entity fields.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    fonts: Optional[List[str]]  # Custom fonts (returned only when `fontsMode` is `manual`).
    macAddress: Optional[Dict[str, Any]]  # MAC-address spoofing settings.
    deviceName: Optional[Dict[str, Any]]  # Device-name spoofing settings.
    audio: Optional[Dict[str, Any]]  # Audio fingerprint settings.
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]  # Report `navigator.doNotTrack = 1`. Take it from the fingerprint object if you do not understand what to put here.
    useragent: Optional[Dict[str, Any]]  # User-Agent spoofing settings.
    webrtc: Optional[Dict[str, Any]]
    canvas: Optional[Dict[str, Any]]
    webgl: Optional[Dict[str, Any]]
    webgpu: Optional[Dict[str, Any]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Dict[str, Any]]
    timezone: Optional[Dict[str, Any]]
    locale: Optional[Dict[str, Any]]
    geolocation: Optional[Dict[str, Any]]
    cpu: Optional[Dict[str, Any]]
    memory: Optional[Dict[str, Any]]
    screen: Optional[Dict[str, Any]]
    connectionDownlink: Optional[Any]  # Reported downlink speed in Mbps.
    connectionEffectiveType: Optional[Any]  # Reported connection type (`4g`, `3g`, …).
    connectionRtt: Optional[Any]  # Reported round-trip time in ms.
    connectionSaveData: Optional[Union[int, Any]]
    platformName: Optional[Any]  # Full platform name reported by the browser fingerprint.
    cpuArchitecture: Optional[Any]  # CPU architecture string reported by the browser fingerprint.
    osVersion: Optional[Any]  # Operating-system version string derived from the fingerprint.
    screenWidth: Optional[Any]  # Reported screen width in pixels (flattened from the screen block).
    screenHeight: Optional[Any]  # Reported screen height in pixels (flattened from the screen block).
    vendorSub: Optional[Any]  # Value of navigator.vendorSub reported by the profile.
    productSub: Optional[Any]  # Value of navigator.productSub reported by the profile.
    vendor: Optional[Any]  # Value of navigator.vendor reported by the profile.
    product: Optional[Any]  # Value of navigator.product reported by the profile.
    appCodeName: Optional[Any]  # Value of navigator.appCodeName reported by the profile.
    mediaDevices: Optional[Any]  # List of media devices returned by navigator.mediaDevices.enumerateDevices().
    userFields: Optional[List[Dict[str, Any]]]  # Arbitrary custom fields supplied by the user; each item is an object with user-defined keys.
    ports: Optional[Dict[str, Any]]  # Port protection settings for the profile.

class BrowserProfileList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class BrowserProfileListItem(TypedDict, total=False):
    """A complete browser profile object. A browser profile emulates a separate, fully-isolated browser instance with its own fingerprint, proxy, cookies, and other persistent data. Most write-operations that reference a browser profile will accept a subset of the fields below – this schema intentionally contains **all** attributes that can be returned by the "List browser profiles" and "Get browser profile" endpoints so that generated clients have full type-safety.
"""
    id: int
    teamId: Optional[int]  # Team identifier that owns the profile.
    userId: Optional[int]  # Identifier of the user that initially created (owns) the profile.
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Optional[Any]  # Host OS version.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Website that is indicated as the main website of the profile in the UI. Used for the profile icon, some spoof tweaks, etc.
    status: Optional[Dict[str, Any]]  # A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI.
    proxy: Optional[Dict[str, Any]]  # A lightweight proxy object embedded inside the browser-profile list payload.
    access: Optional[Dict[str, Any]]  # CRUD permissions of the current user with respect to this profile.
    pinned: Optional[bool]  # Indicates whether the profile is pinned in the UI for the current user.
    folder: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    homepages: Optional[List[Dict[str, Any]]]  # Custom startup pages configured for the profile.
    fontsMode: Optional[str]  # Strategy used for fonts override – `auto` (default) or `manual`.
    macAddress: Optional[Union[Dict[str, Any], str, List[str]]]
    deviceName: Optional[Union[Dict[str, Any], str, List[str]]]
    audio: Optional[Union[Dict[str, Any], List[Any], str]]
    isHiddenProfileName: Optional[bool]  # If `true`, the profile name is hidden in WebGL fingerprint (anti-detection measure).
    disableLoadWebCameraAndCookies: Optional[Any]  # If `true`, the built-in browser will not load a web-camera and will disable cookies.
    enableArgIsChromeIcon: Optional[Any]  # When `true` an additional launch argument is injected so the profile icon mimics Chrome.
    doNotTrack: Optional[bool]
    totalSessionDuration: Optional[int]  # Total time (in seconds) the profile has been running since creation.
    lastStartTime: Optional[Any]  # Date & time when the profile was last started.
    created_at: Optional[str]
    updated_at: Optional[str]  # Timestamp is always returned in Europe/Moscow (UTC+03:00) timezone – the backend converts it from UTC.
    useragent: Optional[Union[Dict[str, Any], str]]
    webrtc: Optional[Union[Dict[str, Any], str]]
    canvas: Optional[Union[Dict[str, Any], str]]
    webgl: Optional[Union[Dict[str, Any], str]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Union[Dict[str, Any], str]]
    timezone: Optional[Union[Dict[str, Any], str]]
    locale: Optional[Union[Dict[str, Any], str]]
    geolocation: Optional[Union[Dict[str, Any], str]]
    cpu: Optional[Union[Dict[str, Any], int]]
    memory: Optional[Union[Dict[str, Any], int]]
    connection: Optional[Dict[str, Any]]
    ports: Optional[Union[List[int], str]]
    storagePath: Optional[str]  # Internal path for browser profile data.
    transferStatus: Optional[Any]  # When the profile is being transferred to another team this field shows the transfer status.
    transferToEmail: Optional[Any]  # Email address of the receiver when the profile transfer is in progress.
    transferHandleDate: Optional[Any]  # Date & time when the transfer request was handled (accepted or cancelled).
    transferWithProxy: Optional[Any]  # Indicates whether the proxy was moved together with the profile during transfer.
    requirePassword: Optional[bool]  # Indicates whether the profile is protected by a password (any modifying request must provide the password).
    recoverCount: Optional[int]  # Number of recovery snapshots available for the profile.
    cloudSyncDisabled: Optional[Any]  # When true, cloud sync is disabled for the profile on the current team account.
    cloudSyncDisabledOnMachineId: Optional[Any]  # Identifier of the machine that disabled cloud sync (if any).
    notes: Optional[Union[Dict[str, Any], str, Any]]

class BrowserProfileFull(TypedDict, total=False):
    """A complete browser-profile object as returned by the "Get browser profile" endpoint.
Contains every attribute currently emitted by the backend. It **extends** the
generic `BrowserProfile` schema with additional fields such as UA version,
WebGPU, advanced device information etc.
"""
    id: int
    teamId: Optional[int]  # Team identifier that owns the profile.
    userId: Optional[int]  # Identifier of the user that initially created (owns) the profile.
    name: str  # Human-readable profile name shown in the UI.
    tags: Optional[List[str]]  # Free-form tags attached to the profile.
    platform: str  # Host OS that the profile mimics.
    platformVersion: Optional[Any]  # Host OS version.
    browserType: str  # Browser engine used by the profile (always `anty`, legacy field).
    mainWebsite: Optional[Any]  # Website that is indicated as the main website of the profile in the UI. Used for the profile icon, some spoof tweaks, etc.
    status: Optional[Dict[str, Any]]  # A custom status label that can be assigned to Browser profiles to quickly group or filter them in the UI.
    proxy: Optional[Dict[str, Any]]  # A proxy configuration object.
    access: Optional[Dict[str, Any]]  # CRUD permissions of the current user with respect to this profile.
    pinned: Optional[bool]  # Indicates whether the profile is pinned in the UI for the current user.
    folder: Optional[Any]  # Identifier of the folder the profile belongs to (if any).
    homepages: Optional[List[Dict[str, Any]]]
    fontsMode: Optional[Any]
    fonts: Optional[List[str]]
    macAddress: Optional[Union[str, List[str], Dict[str, Any]]]
    deviceName: Optional[Union[str, List[str], Dict[str, Any]]]
    audio: Optional[Union[Dict[str, Any], List[Any], str]]
    isHiddenProfileName: Optional[bool]
    disableLoadWebCameraAndCookies: Optional[Any]
    enableArgIsChromeIcon: Optional[Any]
    doNotTrack: Optional[bool]
    totalSessionDuration: Optional[int]  # Total time (in seconds) the profile has been running since creation.
    lastStartTime: Optional[Any]  # Date & time when the profile was last started.
    lastRunUuid: Optional[Any]
    running: Optional[bool]  # Indicates whether the profile is currently running on any user machine.
    created_at: Optional[str]
    updated_at: Optional[str]
    useragent: Optional[Union[Dict[str, Any], str]]
    webrtc: Optional[Union[Dict[str, Any], str]]
    canvas: Optional[Union[Dict[str, Any], str]]
    webgl: Optional[Union[Dict[str, Any], str]]
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` parameter names to their reported values. Each value is either an integer or a two-element integer array (for parameters like `MAX_VIEWPORT_DIMS`).
    webglInfo: Optional[Union[Dict[str, Any], str]]
    clientRect: Optional[Union[Dict[str, Any], str]]
    timezone: Optional[Union[Dict[str, Any], str]]
    locale: Optional[Union[Dict[str, Any], str]]
    geolocation: Optional[Union[Dict[str, Any], str]]
    cpu: Optional[Union[Dict[str, Any], int]]
    memory: Optional[Union[Dict[str, Any], int]]
    screen: Optional[Dict[str, Any]]
    connection: Optional[Dict[str, Any]]
    ports: Optional[Union[List[int], str]]
    storagePath: Optional[str]
    transferStatus: Optional[Any]
    transferToEmail: Optional[Any]  # Email address of the receiver when the profile transfer is in progress.
    transferHandleDate: Optional[Any]  # Date & time when the transfer request was handled (accepted or cancelled).
    transferWithProxy: Optional[Any]  # Indicates whether the proxy was moved together with the profile during transfer.
    requirePassword: Optional[bool]  # Indicates whether the profile is protected by a password (any modifying request must provide the password).
    notes: Optional[Union[Dict[str, Any], str, Any]]
    proxyId: Optional[int]
    uaFullVersion: Optional[str]
    webgpu: Optional[Union[str, Dict[str, Any]]]
    platformName: Optional[Any]
    cpuArchitecture: Optional[Any]
    osVersion: Optional[Any]
    vendorSub: Optional[Any]
    productSub: Optional[Any]
    vendor: Optional[Any]
    product: Optional[Any]
    appCodeName: Optional[Any]
    args: Optional[List[Union[str, float, bool]]]  # Launch arguments that the desktop client will pass to the browser engine.
    tabs: Optional[List[Union[str, float, Dict[str, Any]]]]  # Opened tabs information returned only by the Get-profile endpoint.
    bookmarks: Optional[List[Dict[str, Any]]]  # Team bookmarks applicable to this profile.
    extensions: Optional[List[Dict[str, Any]]]  # Browser extensions associated with this profile.
    userFields: Optional[Dict[str, Any]]
    mediaDevices: Optional[Any]
    cloudSyncDisabled: Optional[Any]
    cloudSyncDisabledOnMachineId: Optional[Any]
    lastRunningTime: Optional[Any]
    lastRunnedByUserId: Optional[Any]
    extensionsNewNaming: Optional[bool]
    login: Optional[Any]
    password: Optional[Any]

class BrowserProfileDeleteInput(TypedDict, total=False):
    browserProfilePassword: Optional[str]  # Profile password. Required only when the targeted Browser profile is protected by a password. If the profile is not password-protected this field MUST be omitted.

    forceDelete: Optional[bool]  # When **true** the profile is permanently removed instead of being moved to the "Basket". Free-plan workspaces must supply this flag to confirm the intent since the basket is not available on free plans. 


class BrowserProfileBulkDeleteInput(TypedDict, total=False):
    ids: List[int]  # Identifiers of Browser profiles to delete.
    browserProfilePassword: Optional[str]  # Profile password. Used only when the request deletes **exactly one** profile and that profile is protected by a password. Must be omitted in all other cases.

    forceDelete: Optional[bool]  # When **true** profiles are permanently removed instead of being moved to the "Basket". Free-plan workspaces must supply this flag to confirm the intent since the basket is not available on free plans. 


class BrowserProfileTransferInput(TypedDict, total=False):
    ids: List[int]  # Identifiers of Browser profiles to transfer. The caller **must** be the owner of these profiles or have the `share` permission granted for them; otherwise the request will be rejected with a 403 error.

    username: str  # E-mail address of the Dolphin{anty} user who will **receive** the transferred profiles. The user may belong to the same team or to a different team/workspace. If the user is not found the request succeeds silently but no transfer is performed (this matches the backend behaviour).

    withProxy: Optional[bool]  # When `true` and a profile has a proxy attached, that proxy object **and its credentials** are moved to the receiver together with the profile. If omitted or set to `false` the profile is transferred **without** a proxy (its `proxyId` is reset to `0`).
Only proxies **owned by the sender team** can be transferred; shared or external proxies cannot be moved and will be stripped from the profile irrespective of this flag. 


class BrowserProfileAccessMultiEditInput(TypedDict, total=False):
    """Input payload for **Share access to multiple browser profiles** endpoint.
Grants or revokes specific CRUD permissions for one or more users across
the selected Browser profiles in bulk.
"""
    ids: List[int]  # List of Browser profile identifiers that should be affected.
    users: List[Dict[str, Any]]  # List of user-permission descriptors. Every object configures permissions
for a single user. When `action` is `add`, the specified permission
flags are **granted** (set to `true`). When `action` is `remove`, the
same flags are **revoked** (set to `false`).

    action: str  # Specifies whether the listed permissions should be **added** (`add`) or
**removed** (`remove`). If `remove` is used, *all* supplied permission
flags must be `true` in order to fully revoke the access row.


class BrowserProfileAccessUpdateInput(TypedDict, total=False):
    """Input payload for **Share access to browser profile** endpoint. Updates
CRUD permissions for one or more users with respect to a **single**
Browser profile.
"""
    users: List[Dict[str, Any]]  # List of user-permission descriptors. Same shape as in the bulk endpoint
but uses the `userId` key as required identifier of the target user.

    browserProfilePassword: Optional[str]  # Profile password (required only when the profile is protected with a
password). Must match the previously set password to allow permission
changes.  
Ignored when profile is not protected. 


class Fingerprint(TypedDict, total=False):
    """A full browser fingerprint snapshot. This structure is returned by the
**“Get fingerprint”** endpoint and is intended to be used as-is when
creating browser profiles.

Most scalar properties are copied verbatim from real-world devices in our
internal dataset – no additional processing is applied. Keep the payload as
is to achieve maximum anti-detect quality.
"""
    screen: Dict[str, Any]  # Detailed screen metrics.
    connection: Dict[str, Any]  # Network connection metrics from the *Network Information API*.
    deviceMemory: float  # Approximate RAM size (GiB).
    hardwareConcurrency: int  # Number of logical CPU cores.
    donottrack: bool  # Reported value of the `navigator.doNotTrack` flag.
    language: str  # Primary user interface language.
    languages: str  # Comma-separated list of preferred languages.
    productSub: str  # Value of `navigator.productSub`.
    vendorSub: str  # Value of `navigator.vendorSub`.
    vendor: str  # Browser vendor.
    appCodeName: str  # Value of `navigator.appCodeName`.
    appVersion: str  # Value of `navigator.appVersion`.
    platform: str  # Host operating system reported by the browser.
    product: str  # Value of `navigator.product`.
    userAgent: str  # Full user-agent string.
    cpu: Dict[str, Any]
    os: Dict[str, Any]
    browser: Dict[str, Any]
    webgl: Dict[str, Any]
    voices: Optional[str]  # JSON-encoded list of `SpeechSynthesisVoice` objects supported by the device.
    fonts: Optional[str]  # JSON-encoded list of fonts installed on the system. Present only when the account has *Fonts override* permission.
    browserType: str  # Browser family for which the fingerprint was generated.
    platformVersion: str  # Internal Dolphin{anty} platform version identifier.
    uaFullVersion: str  # Full UA version retrieved from the *User-Agent Client Hints* API.
    webgl2Maximum: Optional[Dict[str, Any]]  # Mapping of WebGL2 `MAX_*` constants to their reported values. Each value is either an integer or a two-element integer array.
    webgpu: Optional[str]  # Serialized GPU adapter info captured from the *WebGPU* API.

class Font(TypedDict, total=False):
    """A single font record coming from the Dolphin{anty} fingerprint dataset.  
Each entry represents a **font family** that realistically exists on the
specified platform and can therefore be safely used when overriding the
`fonts` fingerprint block.
"""
    id: int  # Unique identifier of this font record inside the dataset.
    font: str  # The full font family name (e.g. the value returned by `Canvas` API or available in CSS `font-family`).
    type: str  # Category describing how common the font is on the target platform.  

- **`default`** – ships with the operating system and is almost always present.  
- **`extra`** – frequently observed additional fonts (may be missing on a clean install).  

Treat the value as an **opaque string** – new categories may appear in the future.

    os: str  # Operating system this font belongs to.

class HomePage(TypedDict, total=False):
    """Homepage record used as a custom start page in Dolphin{anty} browser profiles. Each
homepage points to a specific URL and can optionally be shared with the whole team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the homepage.
    userId: Optional[int]  # Identifier of the user who created the homepage.
    name: str  # Human-readable name shown in the UI (not the URL itself).
    url: str  # Absolute URL the browser opens on startup, including scheme (`https://`).
    sharedToEntireTeam: Optional[bool]  # When `true` the homepage becomes visible and attachable by every member of the team.
When `false` the homepage is private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories indicating where the homepage is primarily used.
This data powers contextual suggestions in the UI.

    created_at: Optional[str]
    updated_at: Optional[str]

class HomePageCreateInput(TypedDict, total=False):
    """Parameters required to create a homepage."""
    name: str  # Human-readable name shown in the UI.
    url: str  # Destination URL to open on browser start.
    sharedToEntireTeam: bool  # Whether to share the homepage with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this homepage.

class HomePageUpdateInput(TypedDict, total=False):
    """Fields identical to creation but intended for partial updates – supply only the attributes you want to change."""
    name: str  # Human-readable name shown in the UI.
    url: str  # Destination URL to open on browser start.
    sharedToEntireTeam: bool  # Whether to share the homepage with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this homepage.

class HomePageList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class HomePageListItem(TypedDict, total=False):
    """Homepage record used as a custom start page in Dolphin{anty} browser profiles. Each
homepage points to a specific URL and can optionally be shared with the whole team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the homepage.
    userId: Optional[int]  # Identifier of the user who created the homepage.
    name: str  # Human-readable name shown in the UI (not the URL itself).
    url: str  # Absolute URL the browser opens on startup, including scheme (`https://`).
    sharedToEntireTeam: Optional[bool]  # When `true` the homepage becomes visible and attachable by every member of the team.
When `false` the homepage is private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories indicating where the homepage is primarily used.
This data powers contextual suggestions in the UI.

    created_at: Optional[str]
    updated_at: Optional[str]

class HomePageBulkDeleteInput(TypedDict, total=False):
    """Delete multiple homepages at once."""
    ids: List[int]  # Identifiers of homepages to delete.

class Bookmark(TypedDict, total=False):
    """Bookmark record used as a custom browser bookmark (quick-access link) inside Dolphin{anty}. A bookmark always points to a particular web page and, when shared, becomes available to every member of the team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the bookmark.
    userId: Optional[int]  # Identifier of the user who created the bookmark.
    name: str  # Human-readable label shown in the Dolphin{anty} UI.
    url: str  # Absolute URL the built-in browser navigates to when the bookmark is clicked.
    favicon: Optional[Any]  # Link to the page favicon. The backend attempts to auto-fetch the icon on creation, therefore this field is usually **null** in the request payload and populated only in the response.

    sharedToEntireTeam: Optional[bool]  # When `true` the bookmark is visible and attachable by **all** team members. When `false` it stays private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories designating the environment where the bookmark is predominantly used. Accepted values are the same as for browser profiles and homepages.

Used for automatically applying the bookmark to the browser profiles with the same main website.

    created_at: Optional[str]
    updated_at: Optional[str]

class BookmarkCreateInput(TypedDict, total=False):
    """Parameters required to create a bookmark."""
    name: str  # Human-readable label shown in the UI.
    url: str  # Destination URL to open when the bookmark is activated.
    sharedToEntireTeam: bool  # Whether to share the bookmark with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this bookmark.

class BookmarkUpdateInput(TypedDict, total=False):
    """Fields identical to creation but intended for partial updates – supply only the attributes you want to change."""
    name: str  # Human-readable label shown in the UI.
    url: str  # Destination URL to open when the bookmark is activated.
    sharedToEntireTeam: bool  # Whether to share the bookmark with the entire team (`true`) or keep it private (`false`).
    mainWebsite: List[str]  # Website category/categories relevant to this bookmark.

class BookmarkList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class BookmarkListItem(TypedDict, total=False):
    """Bookmark record used as a custom browser bookmark (quick-access link) inside Dolphin{anty}. A bookmark always points to a particular web page and, when shared, becomes available to every member of the team.
"""
    id: int
    teamId: Optional[int]  # Identifier of the team that owns the bookmark.
    userId: Optional[int]  # Identifier of the user who created the bookmark.
    name: str  # Human-readable label shown in the Dolphin{anty} UI.
    url: str  # Absolute URL the built-in browser navigates to when the bookmark is clicked.
    favicon: Optional[Any]  # Link to the page favicon. The backend attempts to auto-fetch the icon on creation, therefore this field is usually **null** in the request payload and populated only in the response.

    sharedToEntireTeam: Optional[bool]  # When `true` the bookmark is visible and attachable by **all** team members. When `false` it stays private to the creator.

    mainWebsite: Optional[List[str]]  # One or more "main website" categories designating the environment where the bookmark is predominantly used. Accepted values are the same as for browser profiles and homepages.

Used for automatically applying the bookmark to the browser profiles with the same main website.

    created_at: Optional[str]
    updated_at: Optional[str]

class BookmarkBulkDeleteInput(TypedDict, total=False):
    """Delete multiple bookmarks at once."""
    ids: List[int]  # Identifiers of bookmarks to delete.

class TeamUser(TypedDict, total=False):
    """A team user represents a member of the current team account.
Team members share access to browser profiles, folders and other resources
according to their role and access settings described below.
"""
    id: int  # Unique identifier of the user inside Dolphin{anty}.
    teamId: Optional[int]  # Identifier of the team the user belongs to.
    username: str  # E-mail used to log into Dolphin{anty}.
    displayName: Optional[Any]  # Human-readable name shown in the UI. When null the username is used instead.
    telegram: Optional[Any]  # Telegram username linked to the account (without the `@` sign).
    role: str  # Role of the user inside the team.
• `admin` – full control over the team account
• `teamlead` – manages a subset of users and resources
• `user` – regular member with limited permissions

    teamleads: Optional[List[int]]  # List of identifiers of team-lead users supervising the member.
    access_setting: Optional[Dict[str, Any]]  # Fine-grained limits applied to the user.
    created_at: Optional[str]  # Date & time when the user was created (Europe/Moscow, UTC+03:00).
    updated_at: Optional[str]  # Date & time of the last update (Europe/Moscow, UTC+03:00).

class TeamUserUpdateInput(TypedDict, total=False):
    """Set of fields that can be modified for an existing team user. 
All properties are optional – provide only those you need to change.
"""
    password: Optional[str]  # New login password. When omitted the password is not changed.
    username: Optional[str]  # New login e-mail. Must be unique within Dolphin{anty}.
    displayName: Optional[str]  # New human-readable name shown in the UI.
    role: Optional[str]  # New role to assign to the user.
    teamleads: Optional[List[int]]  # Identifiers of team-lead users supervising the member. Passing an empty array removes supervisors.
    canCreateBp: Optional[bool]  # Grant or revoke the permission to create browser profiles.
    unlimitedBp: Optional[bool]  # When `true` the user is not limited by `bpLimit`.
Must be provided **together** with `canCreateBp=true`.

    bpLimit: Optional[int]  # Hard limit for the amount of browser profiles the user can own.
Ignored when `unlimitedBp` is set to `true`. 


class TeamUserList(TypedDict, total=False):
    current_page: Optional[int]  # Current page number of the results set.
    first_page_url: Optional[str]  # Absolute URL pointing to the first page of results.
    from: Optional[Any]  # Index (1-based) of the first item returned in the current page, or null if the collection is empty.
    last_page: Optional[int]  # Total number of pages available based on the current filter.
    last_page_url: Optional[str]  # Absolute URL pointing to the last page of results.
    next_page_url: Optional[Any]  # Absolute URL for the next page of results, or null if this is the last page.
    path: Optional[str]  # Base path for the paginated resource (without query parameters).
    per_page: Optional[int]  # Maximum number of items returned per page.
    prev_page_url: Optional[Any]  # Absolute URL for the previous page of results, or null if this is the first page.
    to: Optional[Any]  # Index (1-based) of the last item returned in the current page, or null if the collection is empty.
    total: Optional[Union[int, str]]
    data: Optional[List[Dict[str, Any]]]

class TeamUserListItem(TypedDict, total=False):
    """A team user represents a member of the current team account.
Team members share access to browser profiles, folders and other resources
according to their role and access settings described below.
"""
    id: int  # Unique identifier of the user inside Dolphin{anty}.
    teamId: Optional[int]  # Identifier of the team the user belongs to.
    username: str  # E-mail used to log into Dolphin{anty}.
    displayName: Optional[Any]  # Human-readable name shown in the UI. When null the username is used instead.
    telegram: Optional[Any]  # Telegram username linked to the account (without the `@` sign).
    role: str  # Role of the user inside the team.
• `admin` – full control over the team account
• `teamlead` – manages a subset of users and resources
• `user` – regular member with limited permissions

    teamleads: Optional[List[int]]  # List of identifiers of team-lead users supervising the member.
    access_setting: Optional[Dict[str, Any]]  # Fine-grained limits applied to the user.
    created_at: Optional[str]  # Date & time when the user was created (Europe/Moscow, UTC+03:00).
    updated_at: Optional[str]  # Date & time of the last update (Europe/Moscow, UTC+03:00).

class TeamUserCreateInput(TypedDict, total=False):
    """Payload for creating a new member inside the current team account.
Only users with the `admin` role can add team members.
"""
    username: str  # Unique e-mail address used as the login for the new user.
    password: str  # Login password for the new user.
Must be 8–512 characters long.

    role: str  # Role to assign to the new user.
    displayName: Optional[str]  # Human-readable name shown in the UI.
    teamleads: Optional[List[int]]  # Identifiers of team-lead users supervising the member.
Can only be provided when `role` is `user`.

    canCreateBp: Optional[bool]  # Grants the permission to create new browser profiles.
When omitted the permission defaults to the backend logic depending on the requester role.

    unlimitedBp: Optional[bool]  # When `true` the user is not limited by `bpLimit`.
Must be provided **together** with `canCreateBp=true`.

    bpLimit: Optional[int]  # Hard limit for the amount of browser profiles the user can own.
Ignored when `unlimitedBp` is set to `true`. 


class LocalStorageItem(TypedDict, total=False):
    """Single Local Storage snapshot for one origin. When exporting Local Storage the backend
groups key/value pairs by their associated **domain** (origin). Each object therefore
contains data for exactly one domain.
"""
    domain: str  # Origin (domain) the Local Storage belongs to. A special placeholder value
`dolphin-anty-export` is used by the backend when the export represents a
flattened dump that mixes keys from multiple origins.

    data: Dict[str, Any]  # Dictionary of Local Storage entries as they are kept inside Chromium’s
LevelDB. **Both keys and values are Base-64 encoded strings**. Consumers
normally treat this object as an opaque blob – you rarely need to decode
it manually.


class LocalStorageExport(TypedDict, total=False):
    """Complete Local Storage dump produced by the export endpoints. The array
contains one or more `LocalStorageItem` objects – one per origin.
"""
    pass

class LocalStorageImportInput(TypedDict, total=False):
    """Payload accepted by `POST /local-storage/import`.
"""
    profileId: int  # Identifier of the browser profile that should receive the Local Storage.
    localStorage: List[Dict[str, Any]]  # Complete Local Storage dump produced by the export endpoints. The array
contains one or more `LocalStorageItem` objects – one per origin.

    transfer: Union[int, bool]
    plan: str  # Subscription plan of the caller.

    browserProfilePassword: Optional[Any]  # Password protecting the target profile (if `requirePassword` is enabled).
Omit or pass `null` when not used.

    cloudSyncDisabled: Optional[bool]  # When `true` skips downloading the existing datadir from cloud storage and does not
push the archive back after import.


class CookieItem(TypedDict, total=False):
    """Single browser cookie entry as stored in Chromium’s SQLite `Cookies` DB. Each
object represents **one** cookie (name/value pair).
"""
    domain: str  # Hostname the cookie applies to (leading dot allowed for subdomains).
    name: str  # Cookie name.
    value: str  # Raw cookie value.
    path: str  # Resource path scope.
    expirationDate: int  # Expiration timestamp in **milliseconds** since Unix epoch (Chromium format).

    secure: Optional[bool]  # When `true`, the cookie is only sent over HTTPS.
    httpOnly: Optional[bool]  # When `true`, the cookie is inaccessible to JavaScript (`document.cookie`).

    sameSite: Optional[str]  # SameSite attribute controlling cross-site behaviour.

class CookiesExport(TypedDict, total=False):
    """Flat list of cookies produced by the export endpoints. The array contains
zero or more `CookieItem` objects.
"""
    pass

class CookiesImportInput(TypedDict, total=False):
    """Payload accepted by `POST /cookies/import`.
"""
    profileId: int  # Identifier of the browser profile that will receive the cookies.
    cookies: List[Dict[str, Any]]  # Flat list of cookies produced by the export endpoints. The array contains
zero or more `CookieItem` objects.

    transfer: Union[int, bool]
    browserProfilePassword: Optional[Any]  # Password protecting the target profile (if `requirePassword` is enabled).
Omit or pass `null` when not used.

    cloudSyncDisabled: Optional[bool]  # When `true` skips downloading the existing datadir from cloud storage and
does not push the archive back after import.


class CookiesExportInput(TypedDict, total=False):
    """Payload accepted by `POST /export-cookies`.
"""
    browserProfiles: List[Dict[str, Any]]  # Array describing the profiles to export cookies from. Each element must
contain at least the profile `id` and `name`.

    plan: Optional[str]  # Subscription plan of the caller.
    doNotSave: Optional[bool]  # When `true`, the backend does **not** write `.txt` files to the host’s
*Downloads* folder. The cookie data is still returned in the response.


class CookiesExportResponse(TypedDict, total=False):
    """Successful cookies export payload."""
    success: bool
    cookies: List[Dict[str, Any]]  # Flat list of cookies produced by the export endpoints. The array contains
zero or more `CookieItem` objects.


class LoginWithTokenInput(TypedDict, total=False):
    """Payload accepted by `POST /login-with-token`. Stores a
remote Dolphin{anty} **JWT token** inside the Local API and optionally applies
pre-fetched feature flags for the current machine.
"""
    token: str  # The **exact** JWT bearer token generated in the web panel
(https://dolphin-anty.com/panel). The value is stored locally (encrypted
if the OS keychain is available) and will be attached to all subsequent
requests sent by the Local API to the remote Dolphin{anty} endpoints.
