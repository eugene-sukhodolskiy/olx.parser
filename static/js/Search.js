class Search{
	constructor(){
		
	}

	query(searchQuery, callback){
		searchQuery.log();
		ss.get('/rest-api/v1/search?word=' + searchQuery, function(res){
			callback(JSON.parse(res));
		});
	}
}