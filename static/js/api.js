
function postData(keywords, range, position) {
    var data = {
        keywords: keywords,
        range: range,
        position: {
            long: position.coords.longitude,
            lat: position.coords.latitude
        }
    }

    fetch('http://localhost:5000/api/sendDetails',
    {
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
    .then(response => console.log('Success', response))
    .catch(error => console.error('Error:', error));
}