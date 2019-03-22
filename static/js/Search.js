class Search{
	constructor(){
		this.search_api_url = '/rest-api/v1/search?query=';
		// this.search_api_url = '/rest-api/v0/search?query=';
	}

	query(searchQuery, callback){
		searchQuery.log();
		ss.get(this.search_api_url + searchQuery, function(res){
			callback(JSON.parse(res));
		});
	}
}