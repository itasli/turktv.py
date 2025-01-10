# turktv.py

## Description
A REST API built with FastAPI for managing Turkish live stream channels. The project uses [uv](https://github.com/astral-sh/uv) as its package and project manager.

## Project Overview
turktv.py provides a set of RESTful endpoints to manage and serve Turkish live streams. The core functionalities include:
- Channel management
- RESTful API endpoints
- Dynamic playlist generation
- Automated CI/CD pipeline

### Channel Management
Channels are managed through the `ChannelRegistry` class, which maintains information about all available channels. Each channel entry includes essential details such as:
- Channel name
- Logo
- Stream URL

Some stream URLs require dynamic generation, either by:
- Fetching from the live stream page
- Computing based on authentication tokens

### API Endpoints
The application (`main.py`) exposes the following endpoints:
- `/`: Root endpoint returning a basic health check response
- `/favicon.ico`: Serves the application favicon
- `/playlist.m3u`: Generates and serves the M3U playlist
- `/channel/{channel_name}`: Retrieves specific channel details

Channel group routers are modularly organized and registered within the FastAPI application.

### Playlist Generation
The `generate_playlist` function in `app/utils/playlist.py` dynamically creates M3U playlists. The generation process:
1. Retrieves channel information from the `ChannelRegistry`
2. Constructs the M3U file content using the server's base URL
3. Formats the playlist according to M3U specifications

### CI/CD Pipeline
The continuous integration and deployment pipeline handles:
1. Automated testing to ensure code quality
2. Docker image building and publishing
3. Deployment to a virtual machine*

*_Deployment is triggered via a GET request to a local endpoint after establishing a VPN connection._

## Project Status
### Completed Features
- [x] Dockerfile configuration
- [x] CI/CD implementation
  - [x] Docker image pipeline
  - [x] VM deployment
- [x] Test suite
- [x] Documentation
  - [x] Function and class documentation
  - [x] Code comments and annotations
