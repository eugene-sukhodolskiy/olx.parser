class Application{
	constructor(){
		console.log("App start");
		ss('.result-container').hide();

		this.search = new Search();
		this.data = {result: [{title: "Title", price: "price", "page": "url_to_page", "photo": "photo"}]};
		this.ssr = new SSRender('.result-container', this.data);
		this.searchFieldListener();
	}

	renderStart(){
		this.ssr.render();
	}

	searchFieldListener(){
		let self = this;
		ss('.search-field input').on('keydown', function(e){
			if(e.code == 'Enter'){
				ss('.search-field .control').toggleClass('is-loading');
				self.searching(this.value.trim());
			}
		});
	}

	searching(searchQuery){
		let self = this;
		this.search.query(searchQuery, function(response){
			ss('.result-container').show();
			self.data.result = response.result;
			self.ssr.render();
			ss('.search-field .control').toggleClass('is-loading');
		});
	}
}

let app;
window.onload = function(){
	app = new Application();	
	app.renderStart();
}

