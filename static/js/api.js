
// Gets Location using Navigator
function getLocation() {
    var x = document.getElementById("demo");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getInputs);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

// Shows Postion in a html element
function showPosition(position) {
    var x = document.getElementById("demo");
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
}   

// Debug function for testing
function debug(){
    console.log(document.getElementById("keywords").value);
}


// Gathers input from different DOM elements
function getInputs(position) {
    var keywords = document.getElementById("keywords").value;
    var range = document.getElementById("range").value;
    console.log(position);
    if (keywords && range && position) {
        sendRequest(keywords, range, position);
    } else {
        console.log('All fields are NOT filled!')
    }
}

// Sends Request to our Backend API
function sendRequest(keywords, range, position){
    console.log("Sending request...")
    postData(keywords, range, position);
} 

// Handles the onClick event from the submit button
function handleSubmit(){
    getLocation();
}

function createCard(r){
    var newCard = document.createElement("div");
    newCard.setAttribute("class", "card");
    var cardBody = document.createElement("div");
    cardBody.setAttribute("class", "card-body")
    var cardTitle = document.createElement("h5");
    cardTitle.setAttribute("class","card-title")
    cardTitle.innerHTML = r['name'];
    var cardText = document.createElement("p");
    cardText.setAttribute("class", "card-text");
    cardText.innerHTML = `<ul><li>Address: ${r['address']}</li><li>Distance: ${Math.round(r['dis']*100)/100} miles away</li><li><a href="${r['link']}">Menu Link</a</a></li></ul>`;

    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardText);
    newCard.appendChild(cardBody);
    document.getElementById("result").appendChild(newCard);
}


function handleResponse(response){
    console.log("Here")
    console.log('Success',response);
    console.log(response['restaurants'].length);
    document.getElementById('result').innerHTML = '';
    response['restaurants'].map((r) => createCard(r))
}

// Post data to API and handles errors
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
    .then(response => handleResponse(response))
    .catch(error => handleResponse({"restaurants":[]}));
}