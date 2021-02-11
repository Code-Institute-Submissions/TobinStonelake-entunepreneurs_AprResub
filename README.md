# Entunepreneurs

[View the live website here](https://entunepreneurs.herokuapp.com/)

![Homepage](README_files/README_images/indexresp.png)

This is the third Milestone Project for the 
Code Institute's Full Stack Developer course.

In this project, we have been asked to utilise the 
skills that have been developed with HTML, CSS, JavaScript, Python 
and utilising database management systems throughout the course. 
By using these languages and incorporating User input data,
we can create data-based websites that allow
for improved purposes and greater User interaction.
As well as further developing our skills to what is 
expected of a Full Stack Developer and to an industry standard.

As per the standard of Responsive Design, this site is
responsive across a number of devices, making sure to 
be structured in a cohesive manner and change designs
when appropriate. To further achieve this goal, the site
utilises Materialize and MongoDB, aiding its design and performance 
to shape a site that functions seamlessly across a number of devices,
utilises User-input data and broaden the skills and knowledge of the author.

This site, *Entunepreneurs*, allows DJs, Music snobs and the general
User to upload their mixes, setlists and playlists to a database. This 
Functions to allow the User to easily track down songs they may wish to buy,
Simply remember and where it can be found on their local drives. A 
caveat of the digital age, where content is abundant and storage keeps
becoming more accessible, through decreased cost and 
technological advances, it can make it difficult to keep a track of 
the content they wish to seek in the future. This is increasingly difficult
with music libraries due to the increased use of streaming services 
serving as the predominant platform for listening to music.
Having a dualistic quality of making it both easier to access music,
but also narrowing content to be what is available on the service and,
in some cases, making it easy to forget songs that are heard elsewhere.

## UX

### User Stories

* First Time Visitor Goals
    1. As a First Time Visitor, I want to be able to access setlists and libraries
	of other User’s or acts that I am interested in.
1.	As a First Time Visitor, I want to be able to easily sign up and create my own
libraries.
1.	As a First Time Visitor, I want to be able to have CRUD capabilities when 
creating my library.

* Returning and Frequent Visitor Goals
    1. As a Returning or Frequent Visitor, I want to be able to amend, edit and delete 
songs from my playlists and the playlists themselves.
1.	As a Returning or Frequent Visitor, I want to be able to easily search other User’s
databases to see similarities or differences between my own ideas and their own.
1.	As a Returning or Frequent Visitor, I want a singular portal where all of the songs I
wish to listen to, find and purchase can be easily accessed, from anywhere.

* Site Owner Goals
    1. The Site Owner's goal is to utilise digital platforms, to amass trends within
	other User’s data and gain further insights into what other like-minded
	visitors are visiting the site for.
1.	The Site Owner's goal will be to improve their ability to keep track of their
own collections and wishlists.
1.	The Site Owner wants to add to the ever-growing list of 3rd-party sites that
help to promote the services of content producers and are easily linkable within
their own social media and other media platforms. 

### Design

* Colour Scheme
    * The colour scheme used has been akin to the author's signature preference
        to creating 'Dark Mode' aesthetic websites.
    * The author has chosen a cyan and grey base for the majority of elements. 
        Utilising red as a contrasting colour for the background image and 
        appropriate flash messages.
    * By the choice of an unorthodox colour scheme, it also helps to define
        the content, while still keeping a uniformed style across all pages.

* Typography
    * Three fonts have been used across the site. 'Righteous' is the brand font 
        used throughout the website this sets the brand logo and footer to be cohesive.
    * For the h1 tags, 'Alfa Slab One' has been used due to its boldness and dominating
        apperance over the background image. Using cursive as a fallback.
    * For the main text throughout the site, 'Pathway Gothic One' has been used.
        This is a *serious* font that adheres to the conventions of dance-music sites and
        their uniformed aesthetic. This clearly defines head elements as being separate 
        from the main text elements. Using sans-serif as a fallback.

* Imagery
    * The only image used on the site is for the background. This has been taken from
    PixaBay.

* Wireframes
    * [Wireframe](README_files/milestone_3.pdf)

* Database Diagram
    * [Diagram](README_files/entunepreneursDBlink.pdf) or here to see the live version [Live](https://dbdiagram.io/d/6024290380d742080a3a0a69)

## Features

* Responsive across all devices.

* Interactive elements:
    * The driving goal of this site was to allows users to input data that is relevant to
        their musical endeavours.
    * On the Homepage, the User can view all and search through all sets that are available.
        Once logged in, the User also has the opportunity to amend sets and tracks they have uploaded.           
    * On the Register page, the User can create an account, giving them the ability to fully 
        interact with the site.
    * On the relevant Add pages, the User has the opportunity to add any data that they
        they wish to input into the site.
    * On the relevant Edit pages, the User has the opportunity to edit any data that they
        they have input into the site.
    * The Logout function allows a user to cancel their interaction with the site.

### Features left to implement

* In the future I would like to also include links to a YouTube channel and look at their 
    developer tools to see if a 'Widget', similar to that of the Facebook one that can
    be found on the Homepage, or whether it can be embedded and automatically updated by
    their developer tools alone.
* I also would have liked to have included bespoke custom markers, that give a little more 
    information on the Google Map, but I have not been able to figure this out effectively. 

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.5:](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Lily Script One' and 'Yanone Kaffeesatz' fonts into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive and other Bootstrap functions.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [GoogleMaps:](https://developers.google.com/maps/documentation/javascript/overview)
    - Google Maps has been implemented to show the User where a number of fictitious events are
        taking place and highlight the author's ability to use JavaScript to create custom, marked locations. 
1. [EmailJS:](https://www.emailjs.com/)
    - EmailJS has been implemented to allow for an automated emailing service and contact form. This allows
        User's to easily contact the author and be provided with an automated response upon sending their request.
1. [Soundcloud:](https://www.soundcloud.com)
    - Soundcloud has been used to embed the author's tracks and recordings, which will be updated as the author
        updates each respective playlist.
1. [Elfsight:](https://elfsight.com/)
    - Elfsight's Facebook 'Widget' was used to create further interactivity on the Homepage. This was chosen due
        to the nature of the website wanting to be consistently updated across all other relevant sites that are
        attached to *Jig & Thonic*.
1. [Canva:](https://www.canva.com/)
    - Canva has been used to create any logos or images that include *Jig & Thonic*.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://en.wikipedia.org/wiki/Website_wireframe) during the design process.
1. [Microsoft Word:](https://www.microsoft.com/en-gb/microsoft-365/word)
    - Was used to write the content and ensure that the grammatical nature of the content was preserved.    

## Testing

### Testing User Stories from User Experience (UX) Section

**Disclaimer: All testing screenshots can be found after the relevant entry via a link.**

* First Time Visitor Goals
    1. As a First Time Visitor, I want to be able to hear the abilities
        of *Jig & Thonic* and reach their predominant social sites easily.

        1. On the Hompage, a Facebook Widget has been included. This includes the latest 
        posts by *Jig & Thonic* and their recordings and events. [Facebook Widget Screenshot](assets/README_files/README_images/facebookwidget.png)
        2. On the Tracks page, embedded Soundcloud players are included. 
        Allowing User's to easily reach the predominant platform where *Jig & Thonic* upload
        their music. [Player Screenshot](assets/README_files/README_images/tracksimg.png)
        3. At the Footer on each page, links to the relevant social sites can be easily found.
        Utilising the icons of both sites to indicate where the User will be visiting. [Footer Social Screenshot](assets/README_files/README_images/socialimg.png)

    1. As a First Time Visitor, I want to be able to have access to the content
        produced by *Jig & Thonic* on one site, without having to visit several
        different sites.

        1. The Navigation bar on each page clearly and distinctly leads the User to the relevant
        page that they are looking for. [Navbar Screenshot](assets/README_files/README_images/navbarimg.png)
        2. The benefit of using the Facebook widget and the Soundcloud embedded players is that it
        give User's the latest updates without any extra coding required across this page. Therfore,
        this aim is reached through their implementation. *Refer to above Facebook widget screenshot and the Player screenshot.
        3. By creating a centralised hub of *Jig & Thonic's* activity, it achieves this aim well and
        allows Users to also easily contact the author. Either through the contact form or their preferred social
        media avenue.  [Contact Form Screenshot](assets/README_files/README_images/contactimg.png)

    1. As a First Time Visitor, I want to be able to easily contact *Jig & Thonic*
        with queries and ensure that a response will be given back within a declared
        timeframe.

        1. The Contact page utilises EmailJS, which sends an automated response to the user 
        once their query has been submitted.   [Auto-reply Screenshot](assets/README_files/README_images/emailjsautoreply.png)
        2. The timeframe is declared on both the auto-reply and on the contact page itself.
        [Auto-reply Screenshot](assets/README_files/README_images/contactnotice.png) 

* Returning and Frequent Visitor Goals
    1. As a Returning or Frequent Visitor, I want to be able to view the progression of the author's work.
        Periodically and dynamically.

        1. As the user returns to the site, the site will be updated with *Jig & Thonic's* latest
        news, events and recordings.

    1. As a Returning or Frequent Visitor, I want to be able to easily contact the author to be able to 
        collaborate and gain any extra information that they would like.

        1. There is a contact page that can be easily accessed from the navigation bar.
        2. The use of EmailJS ensures that the User's request is easily highlighted to the author
        and ensures that they will be responded to.
        3. A necessary caveat of being successful within the Club/Bar scene (the author's preferred setting),
        is that they are easily reachable to improve the employability prospects within this sector.

    1. As a Returning or Frequent Visitor, I want a singular portal where all of *Jig & Thonic's*
        material can be found and, thus, easily shared between others. 

        1. The nature of the modern world and its increased use of mobile technology means that a singular 
        hub is more important than ever. This ensures that a User has an easy to reach platform and does not
        require them to jump across multiple apps or pages to reach all of *Jig & Thonic's* content.
        2. Because of this singular, centralised hub of content. Users can easily share the page to
        others who may be interested in the site or conveyed their interest towards *Jig & Thonic*, via one link.

* Site Owner Goals
    1. The Site Owner's goal is to utilise digital platforms, particularly
        Social Media and other user-focused Content/Media sites to create
        a hub in which all of the promotional material can be found on one
        site.

        1. This aim is reached by the provision of the relevant developer tools from each site and their implementation.
        2. By using cross-platform services, the Site Owner has the ability to cater these tools themselves.
        As mentioned in the CSS, the Facebook widget had to be stylised within their own environment. This is indicated 
        through the following screenshot and achieved by using the inspect element tool on Google Chrome. 
        [Elfsight CSS Screenshot](assets/README_files/README_images/elfsightcustomisation.png) 

    1. The Site Owner's goal will be to improve their ability 
        to be competitive within the dynamic and saturated DJ 
        market. This will be achieved by making contact easy and, as
        aforementioned, reach their other sites easily.

        1. By the use of a centralised hub, the author can easily showcase any and all work
        that has gone into *Jig & Thonic*. This makes it easy for prospective clients to gain an indication
        of their abilities and make an informed decision towards the viability of *Jig & Thonic* for their needs.
        2. Because of this, it saves both the client and *Jig & Thonic* time in ensuring that an efficient
        and effective service is delivered. Backed by the use of social media to indicate their presence and as a
        portfolio of work.
        3. By using an automated email service, clients can easily contact the author to create a correspondence.
        This greatly improves the financial prospects towards their service becoming used. 

    1. The Site Owner's want to promote themselves effortlessly and 
        effectively, via the use of a centralised website.

        1. This is the main focal point of the site's creation. Once the author's skillset has been further
        developed and extra content is created and uploaded to sites such as YouTube, Spotify and Mixcloud,
        the author will also implement these via their respective development tools.
        2. This can also be said for a shopping basket with different services that can be offered. For the
        moment, the author was advised to wait until their skillset was further developed with the Code Institute,
        as this will be a necessary criterion in a later module.

### Achieved Testing

* Throughout the project, I have been viewing my site across a
number of devices. Including mobiles, tablets, a range of monitors
with different ratios and utilising the inspect element capability 
on Google Chrome to give me further insight into how the site 
functions across devices that I do not have access to.

* During this period, my main focus was to ensure that the site 
was responsive, followed its theme and was as visually appealing
and useable across all devices.

* My largest issue has been with the footer image. This required several tweaks
to ensure that the footer looked and responded well across all media queries.

* EmailJS has been tested and deployed on the site as it works as expected. Emails
can be sent and an auto-reply is received.

* Checked all links across all pages lead to the relevant pages.

* All external links open a new tab using the _blank attribute.

### Further Testing

* The font size may need to be tweaked to ensure that readability is preserved across all
devices.

### Known Issues

* There are some final little aesthetic issues that I would like to fix:
    * The footer copyright text can become a tad too small when viewed on certain devices.
    * Text can appear quite large on smaller devices.
    * On some devices, the Contact Page footer image is very large.

* The Products page, as seen by previous commits,
seems to double up when adding to the basket at the bottom. Due to tutor support, this page
has been omitted as it was informed that this would be a criterion for a future project and
be a smoother feature to add once the relevant languages and skills have been learnt.
Created by referring to this video: https://www.youtube.com/watch?v=YeFzkC2awTM

### Screenshots across different devices

#### Homepage/Index
![Homepage](assets/README_files/README_images/indexresp.png)

#### Tracks
![Tracks Page](assets/README_files/README_images/tracksresp.png)

#### Events
![Events Page](assets/README_files/README_images/eventsresp.png)

#### Contact
![Contact Page](assets/README_files/README_images/contactresp.png)

### W3 Validators

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page. 
This led to a number of errors being present and resolutions needed to overcome said issues.
Evidence of these tests can be found below:

* As a side note, at the time of writing I had two errors that were unable to be fixed until
assurance is provided by my mentor or student support. One is that I get an error due to the
use of the type attribute when linking JavaScript resources. The other is that I get a failure
on the tracks page due to the embedded styling found on the Soundcloud players. It notes that 
this should be in the CSS folder.

#### CSS

![CSS Test](assets/README_files/README_images/cssvalid.png)

#### Index HTML

![Index Test](assets/README_files/README_images/indexvalid.png)

#### Tracks HTML

![Tracks Test](assets/README_files/README_images/tracksvalid.png)

#### Events HTML

![Events Test](assets/README_files/README_images/eventsvalid.png)

#### Contact HTML

![Contact Test](assets/README_files/README_images/contactvalid.png)

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Content

All content has been written or created by the author. This includes all
music, images and text found across the site. 

### Media

Any media that has been used across the site has either been created by
the author, on Reason Studios or with Canva.

### Acknowledgements

* Thanks to my housemate, girlfriend, mother and other friends in looking at this project 
and conveying that they can view the content and access the interactive functions on their own devices.

* Thanks to my Code Institute Tutor, Mentor and Student Support team in offering me advice and support
during the creation of this project.

* I have utilised extra information to allow me to create this page from
Bootstrap's documentation, the relevant developer tools from each site, and articles that can be found on W3. 

* For minor issues, I have read through the Code Institute's material, 
its Slack channels and, as a last resort, forum posts in Stack Overflow.

* To standardise the formatting of my HTML and CSS code, I used https://www.freeformatter.com/html-formatter.html#ad-output and https://www.freeformatter.com/css-beautifier.html#ad-output

#### Port Used To View Real-Time Edits

python3 -m http.server
