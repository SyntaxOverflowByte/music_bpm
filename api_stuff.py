Web API Base URL: https://api.getsongbpm.com
Method: GET

Endpoint	Params	Returns
/search/	
api_key (required): your API key
type (required): "song", "artist" or "both"
lookup (required): Song title (urlencoded) or Artist name (urlencoded), depending on selected type.
For "both" type, prepend searched terms with "song:" and "artist:", like that: lookup=song:enter+sandman artist:metallica
Array of song(s) or artist(s) matching your query.

/artist/	
api_key (required): your API key
id (required): artist ID
Artist infos.

/song/	
api_key (required): your API key
id (required): song ID
Details about a song.