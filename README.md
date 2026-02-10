# Gemini Folders Extension

A Chrome Extension that allows you to organize your Google Gemini chats into custom folders. This extension runs completely locally and stores data in your browser's local storage.

## Features

-   **Create Projects/Folders**: Organize your chats into named projects with custom icons and colors.
-   **Drag and Drop**: Although primarily menu-based now for reliability, basic drag-and-drop support is included.
-   **Context Menu "Move to Project"**: Easily move chats to projects by clicking the three dots menu on any chat item.
-   **Privacy Focused**: All data is stored locally in `chrome.storage.local`. No external servers are involved.
-   **Native UI**: Designed to look and feel exactly like the native Gemini interface.

## Installation

### Prerequisites

-   Use a Chromium-based browser (Chrome, Edge, Brave, etc.).
-   Have `npm` (Node.js) installed to build the project.

### Building from Source

1.  Clone this repository:
    ```bash
    git clone https://github.com/naumansiba/gemini-folders.git
    cd gemini-folders
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Build the extension:
    ```bash
    npm run build
    ```
    This will generate a `dist` folder containing the compiled extension.

### Loading into Chrome

1.  Open your browser and navigate to `chrome://extensions`.
2.  Enable **Developer mode** (toggle in the top right corner).
3.  Click **Load unpacked**.
4.  Select the `dist` folder inside the project directory.
5.  Go to [gemini.google.com](https://gemini.google.com) and refresh the page.

## Usage

1.  **Sidebar Panel**: You will see a new "Projects" section in the left sidebar.
2.  **Create Project**: Click "New Project" to create a folder. You can choose an icon and color.
3.  **Move Chats**: 
    -   Click the three dots (`...`) on any chat in your history.
    -   Select **Move to Project** from the menu.
    -   Choose the destination project.
4.  **Manage Projects**: Click the three dots next to a project name to rename or delete it.

## Development

The project is built with TypeScript and Vite.

-   `src/content`: Content scripts that inject the UI into Gemini.
-   `src/background`: Background service worker.
-   `src/shared`: Shared types and utilities.

To work on the extension, run `npm run watch` (if configured) or rebuild after changes with `npm run build`.

## License

MIT
