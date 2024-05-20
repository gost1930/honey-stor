// Get Slider Items | Array.from [ES6 Feature]
var sliderImage = Array.from(document.querySelectorAll('.slider-container img'));

// Get Number Of Slide
var slidesCount = sliderImage.length

// Set Current Slide 
var currentSlide = 1;

// Slide Number Element
var slideNumberElement = document.getElementById('salde-number')

// Previous and Next Buttons
var nextButton = document.getElementById('next')
var prevtButton = document.getElementById('prev')

// Handling Click on Privious and Next Buttons
nextButton.onclick = nextSlide
prevtButton.onclick = previousSlide


// Create Main Ul Element
var paginationElement = document.createElement('ul')

// Set Id On Creat Ul Element 
paginationElement.setAttribute('id' , 'pagination-ul')

//  Create List Items Based On Slides Count
for (var i = 1 ; i<= slidesCount ; i++){

    // Creat Li
    var paginationItem = document.createElement('li');

    // Set Custom Attribute
    paginationItem.setAttribute('data-index',i)

    // Set Item Content
    paginationItem.appendChild(document.createTextNode(i))

    // Append Item to The Main Ul List
    paginationElement.appendChild(paginationItem)
}

// Add The Created Ul Element to The Page
document.getElementById('indicators').appendChild(paginationElement)

// Get the new creatf Ul
var paginationCreatedUl = document.getElementById('pagination-ul');

// Get pagination Items | Array.from [ES6 Feature]
var paginationsBullets = Array.from(document.querySelectorAll('#pagination-ul li'));

// trigger the checker function
theChecker()

// Next Slide Function
function nextSlide(){
if (nextButton.classList.contains('disable')) {
    return false;
} else {
    currentSlide++;
    theChecker();
}
}
// previous Slide Function
function previousSlide(){
    if (prevtButton.classList.contains('disable')) {
        return false;
    } else {
        currentSlide--;
        theChecker();
    }
}

// Create The checker Function
function theChecker() {
    slideNumberElement.textContent = `Slide # ${currentSlide}  of  ${slidesCount}`;
   // remove all active classes
        removeAllAcrive();
    // set active class on current slide
    sliderImage[currentSlide - 1].classList.add('active');

    // set active class on current pagination item
    paginationCreatedUl.children[currentSlide - 1 ].classList.add('active')

    // check if current slide is the first 
    if (currentSlide  == 1) {
        
        // add disabled class on previous button
        prevtButton.classList.add('disable')

    } else{
         // remove disabled class from previous button
         prevtButton.classList.remove('disable')

    }
    // check if current slide is the Last
    if (currentSlide  == slidesCount ) {
        
        // add disabled class on net button
        nextButton.classList.add('disable')

    } else{
         // remove disabled class from next button
         nextButton.classList.remove('disable')

    }
     
}

// remove all  active classes from  image and pagination bullets
function removeAllAcrive(){
    // Loop Through Images
    sliderImage.forEach(function (img) {
        img.classList.remove('active')
    })

        // Loop Through Pagination Img
        paginationsBullets.forEach(function (bullets) {
            bullets.classList.remove('active')
        })

}