export default class ApiConnector {
    constructor() {
        this.base_url = "http://127.0.0.1:8000";
    }
    searchMovies(query) {
        let url = `${this.base_url}/search_movies_by_name/${query.query}`
        return new Promise(function (resolve, reject) {
            console.log(url)
            console.log(url)
            fetch(url, {method:"GET",
        headers:{
            "Access-Control-Allow-Origin": "*",
        }})
                .then(response => resolve(response.json()))
                .catch(error => console.log(error.txt()))
        })
    }
}