# WebPage Scraper

<div id="top"></div>
<div align="center">
  
![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/License-MIT-blue)
![](https://img.shields.io/github/issues/mstatt/Emotion_Detection)
![](https://img.shields.io/github/forks/mstatt/Emotion_Detection)
  
</div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mstatt/">
    <img src="assets/falcons-logo2.png" alt="Logo" >
  </a>

  <h3 align="center">
WebPage scraper</h3>

  <p align="center">
    A simple script to scrape webpage text.
    <br />

  </p>
</div>




<!-- ABOUT THE PROJECT -->
## About The Emotion Detection Application by Falcons.ai

In this project I wanted to provide a quick and easy python web scraper for those that have ran into issues trying this from other tutorials.


Use this `README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This application was built using Anaconda Python and Beautiful Soup.

* [Anaconda Python](https://www.anaconda.com/products/individual)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to get this project up and running it is assumed that you have downloaded and installed Anaconda Python and updated all dependencies to their latest versions.

### Prerequisites

After installing Anaconda Python the command below will update the packages for you using the terminal or cmd prompt.
* Anaconda Python
  ```sh
  conda --update-all
  ```
  
 Create a new Python enviorment using the requirements.txt file.
* Create New Env
  ```sh
  conda create --name <env_name> 
  ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

 Activate the enviornment.
* Once you created the enviornment, you need to activate it using the following command.
  ```sh
  conda activate <env_name>
  ```
* Once activated install Beautiful Soup
 ```
   pip install beautifulsoup4
 ```

 Launch the application.
* Edit the "single_web_scrape.py" on line 9: url = '<URL>', replace <URL> with the url for the page you would like to scrape. save the file once updated. Ensure that you have created the directory named (scrapes).Now run the following command in the terminal.
  ```sh
  python single_web_scrape.py
  ```
 


<!-- OUTPUT -->
## Output

In the scrapes directory you should see a file titled something like "6a314ebb-af03-431b-96e6-1ac3f187c151.txt". In there should be the text contents of the webpage set in the URL parameter.




<p align="right">(<a href="#top">back to top</a>)</p>



See the https://github.com/mstatt/ a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

[![Licence][license-shield]][license-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/mstatt/]


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: assets/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f74686e65696c647265772f426573742d524541444d452d54656d706c6174652e7376673f7374796c653d666f722d7468652d6261646765.svg?style=for-the-badge
[license-url]: https://github.com/mstatt/Emotion_Detection/blob/main/LICENSE.txt