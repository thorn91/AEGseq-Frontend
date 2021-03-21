# AEGSeq Frontend Proof of Concept

## Overview

Instead of writing a standalone app or manually implemented a socket server to 
allow communication between Python, JavaScript, and HTML changes, EEL provides a
simple interface to allow direct Python <--> Javascript interaction by exposing
functions.  

JavaScript is largely in charge of receiving information, such as filenames, and
Python allows OS interaction outside of the browser sandbox.  It can then pass
information back up to JS to display in the GUI.

## Installation & Running

### Installation 

From within the main AEGseq directory:

`pip install -r requirements.txt` - install Python requirements

### Running

From within the main AEGseq directory:

`python server.py`

