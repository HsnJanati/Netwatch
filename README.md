# NetWatch

NetWatch is a network monitoring and security dashboard developed as a team project.

The goal of the project is to scan and monitor hosts and network services,
store scan results, and display them through a simple web dashboard.

## Features

Planned features:

- Add and manage hosts/IP addresses
- Check whether hosts are reachable
- Scan selected ports and services
- Store scan results and timestamps
- View previous scan results
- Display network information in a web dashboard
- Filter and search scan results

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- TypeScript
- Git / GitHub
- Docker (planned)

## Architecture

The application consists of three main components:

1. **Network Scanner**
   - Performs network and port checks.

2. **Backend API**
   - Provides a REST API using FastAPI.
   - Handles communication between the scanner, database and frontend.

3. **Web Dashboard**
   - Displays hosts, services and scan results.

## Project Structure

Planned structure:

netwatch/
├── backend/
├── frontend/
├── scanner/
├── tests/
├── docs/
└── README.md

## Development

This project is developed collaboratively using:

- GitHub Issues for tasks
- Feature branches
- Pull Requests
- Code Reviews

## Status

🚧 Project currently under development.

## Team

Developed by a team of three computer science students.
