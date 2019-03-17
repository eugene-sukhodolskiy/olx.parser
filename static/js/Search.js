class Search{
	constructor(){
		
	}

	query(searchQuery, callback){
		searchQuery.log();
		ss.get('/static/test-data.json', function(res){
			callback(JSON.parse(res));
		});
	}
}