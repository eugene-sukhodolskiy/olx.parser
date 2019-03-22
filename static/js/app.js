class Application{
	constructor(){
		console.log("App start");
		this.search = new Search();
		this.data = {result: [{title: "Title", price: "price", currency: "currency", is_exchange: "is_exchange", is_promoted: "is_promoted", url: "url_to_page", thumb: "photo"}]};
		this.ssr = new SSRender('.result-container', this.data);
		this.searchFieldListener();
	}

	renderStart(){
		ss('.result-container').hide();
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
			self.data.result = response.products;
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

