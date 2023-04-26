 // Function to call the Lambda function
 var callLambda = () => {
    fetch("INSERT YOUR API GTW INVOKE URL HERE")
    .then(response => response.json())
    .then(result => {
        var quoteElement = document.getElementById("quoteElement");
        quoteElement.innerText = result.quote;

        var imageElement = document.getElementById("imageElement");
        imageElement.src = result.poster_image;
    })
    .catch(error => console.log('error', error));
}

// Call the Lambda function when the web page is loaded or refreshed
window.onload = () => {
    callLambda();
}