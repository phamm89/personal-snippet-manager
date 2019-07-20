// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}


// Variables
let input
let searchURL
const searchForm = q('#searchForm')
const searchButton = q('#searchButton')
const searchBar = q('#searchBar')


// When user releases Enter key, act as if submit button has been clicked
searchForm.addEventListener('keyup', function(event){
    if(event.keyCode === 'Enter'){
        event.preventDefault()
        searchButton.click()
    }
})


// Function to display search results
function getSearch(codes){

    const resultsDiv = document.createElement('div')
    resultsDiv.setAttribute("id", "resultsDiv")
    resultsDiv.innerHTML = `
            <div class='ba bg-blue white'>
                <p><strong>${codes.title}</strong></p>
                <a class='f6 link mt5 dim br3 ph3 pv2 mb2 dib white bg-dark-blue' href="{{ codes.get_absolute_url }}">Edit</a>
                <a class="f6 link mt5 dim br3 ph3 pv2 mb2 dib white bg-dark-blue" href="{% url 'add_snippet' %}">Add New</a>
                <a class="f6 link mt5 dim br3 ph3 pv2 mb2 dib white bg-dark-blue" href="{% url 'delete_snippet' %}">Delete</a>
            </div>
            <div>
                <p>by ${codes.creator}</p>
                <p>added ${codes.date_added}</p>
            </div>
            <div>
                <p> Language: ${codes.languages}</p>
            </div>
            <div><pre><code class='language-${codes.languages}'>
                <p>${codes.code }</p>
            </code></pre>
            </div>
    `

    return resultsDiv
}


// Main execution
document.addEventListener('DOMContentLoaded', function() {

    // Execution for generating list of results upon search button clicked or enter key pressed
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault()
        input = encodeURIComponent(searchBar.value)
        searchURL = `http://localhost:8000/?search=${(input)}`

        fetch(searchURL)
            .then(response => response.json())
            .then(function (data) {
                console.log(data)
                searchResults.innerHTML = ''

                
                for (let codes of data.results){
                    searchResults.appendChild(getSearch(codes))
                }
        })
    })
})
