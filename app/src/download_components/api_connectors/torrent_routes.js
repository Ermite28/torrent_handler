import env from "react-dotenv"


export function searchMovies(query) {
    let url = `${env.API_URL}/search_movies_by_name/${query.query}`
    return new Promise(function (resolve, reject) {
        console.log(url)
        console.log(url)
        fetch(url, {
            method: "GET",
            headers: {
                "Access-Control-Allow-Origin": env.API_URL,
            }
        })
            .then(response => resolve(response.json()))
            .catch(error => console.log(error.txt()))
    })
}

export function getMovieTorrents(movie, site = "yts", limit = 2) {
    let url = `${env.API_URL}/scrap_by_name/${movie.title}?site=${site}`
    return new Promise(function (resolve, reject) {
        console.log(url)
        console.log(url)
        fetch(url, {
            method: "GET",
            headers: {
                "Access-Control-Allow-Origin": env.API_URL,
            }
        })
            .then(response => resolve(response.json()))
            .catch(error => console.log(error.txt()))
    })
}

export function downloadTorrent(movie) {

    getMovieTorrents(movie)
        .then((result) => {
            let requestOptions = {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": env.API_URL,
                },
                body: JSON.stringify(result),
                redirect: 'follow',
              };
              fetch(`${env.API_URL}/new_torrent/`, requestOptions).then(response => response.text()
                                                                                .then(result => console.log(result))
                                                                                .catch(error => console.log(error))) })
        .catch((error) => console.log(error.txt()))
}