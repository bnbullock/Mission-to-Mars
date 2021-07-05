# Mission to Mars


## Project Overview

Our Client has asked us to build a web application encompassing specific features of the planet Mars. It is her desire to impress NASA with a comprehensive website containing facts about the "red planet" featured with images and facts from NASA's own websites and displaying them in a more comprehensive manner. For this specific project we are asked to retrieve hemispheric images and titles, store the information in a local Mongo database, insert them into the website in the correct section and perform customizations on the format of the final result.

- Deliverables:
  1. Scrape of Full-Resolution Mars Hemisphere Images and Titles
  2. Update the Web App with Mars Hemispheric Images and Titles
  3. Add additional Bootstrap 3 Components
------------------------------------------------------------------------------------------------------------

## Resources
- https://data-class-mars.s3.amazonaws.com/Mars/index.html
- https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html
- https://marshemispheres.com
- Database: Mongo DB v4.4.6
- Software: Python 3.7.10, Visual Studio Code 1.56.2, Jupyter Notebook Server 6.3.0, SQLAlchemy 1.4.7, Flask 1.1.2
------------------------------------------------------------------------------------------------------------

## Results

### Scrape of Hemispheric Images and Titles

- Using different scraping techniques we were able to visit the site "marshemispheres" using splinter and inspect the proper tag location of the information we needed. We were then able to capture each image URL and related title required for our web application from the different pages of this site.

### Update the Web App

- The web application could then use the updated scraping function to allocate storage in the Mongo Db for the new hemispheric information intended for adding to the website as requested by the client. Using this new updated route required that we save the hemispheric scraping as a new function that could be accessed by the Web App. We are then able to populate the index.html hemispheres information and diplay them on the website as images.


### Add Bootstrap Components

- We added te following features:
  - Added mobile-responsiveness for different devices
  - Reduced the Hemispheric images to smaller size with width="200"
  - Increased the Mars Facts table for a larger width and added mobile responsiveness
  - Moved the Memisphere title to above the image
  - Changed the background color for Mission to Mars jumbotron
  - Colorized section titles
------------------------------------------------------------------------------------------------------------

## Summary Analysis

- The display results have generally met the deliverables and the site performed as expected. Additional website images and content can be easily added using the framework encompassed in this design. Many different stylized elements can be also added for additional viewability as required.