# RuneLite JavaDoc Scraper

A Python-based web scraper that extracts JavaDoc content from the RuneLite API documentation and converts it to well-formatted markdown for LLM consumption.

## 🎯 Overview

This project scrapes all RuneLite API classes and interfaces from the official JavaDoc documentation located at `https://static.runelite.net/runelite-api/apidocs/` and provides them in two formats:
- **Individual files**: One `.md` file per class/interface
- **Consolidated file**: `ALL_RUNELITE_DOCS.md` with everything in one organized document

## ✨ Features

- 🕷️ **Automatic Discovery**: Automatically discovers all RuneLite API classes from the documentation index
- 📝 **Clean Markdown**: Converts HTML to well-formatted, LLM-friendly markdown
- 🎯 **Dual Output**: Creates both individual files and a consolidated document
- ⚡ **Rate Limiting**: Respectful 1-second delay between requests
- 📊 **Progress Tracking**: Visual progress bars and detailed error reporting
- 🔍 **Metadata Extraction**: Class names, packages, descriptions, and URLs
- 📋 **Table of Contents**: Clickable navigation in the consolidated file

## 📁 Repository Contents

### Core Files
- `scraper.py` - Main scraper class with all functionality
- `main.py` - Command-line interface script
- `urls.py` - URL discovery and list of RuneLite API URLs
- `requirements.txt` - Python dependencies

### Documentation Output
- `scraped_docs/` - Directory containing all scraped documentation
  - `ALL_RUNELITE_DOCS.md` - **Consolidated file with all pages**
  - Individual `.md` files for each class/interface
  - `scraping_summary.json` - Statistics and metadata

## 🚀 Quick Start

### Installation
```bash
git clone <repository-url>
cd tribot-docs-scraper
pip install -r requirements.txt
```

### Usage

**Scrape all RuneLite API pages (default):**
```bash
python main.py
```

**Test with single page:**
```bash
python main.py --test
```

**Custom options:**
```bash
python main.py --output my_docs --delay 2.0
```

## 📊 Scraping Results

The scraper automatically discovers all available RuneLite API documentation pages and processes them:

- ✅ **Automatic URL discovery** from overview-tree.html
- 📄 **Individual markdown files** for each class/interface
- 📚 **1 consolidated file** (`ALL_RUNELITE_DOCS.md`)

## 📖 Output Format

### Individual Files
Each class gets its own markdown file with:
- Class/interface name as main heading
- Source URL and package information
- Description (if available)
- Complete JavaDoc content in markdown format

### Consolidated File
The `ALL_RUNELITE_DOCS.md` file includes:
- **Header** with generation timestamp and page count
- **Table of Contents** with clickable links to each class
- **Individual sections** for each discovered class
- **Clear separators** and navigation between pages

## 🛠️ Technical Details

### Dependencies
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML parser
- `markdownify` - HTML to markdown conversion
- `tqdm` - Progress bars

### URL Discovery
The scraper automatically discovers all class URLs by parsing the `overview-tree.html` page from the RuneLite API documentation. This ensures you always get the latest classes without manually maintaining a URL list.

### Rate Limiting
- 1-second delay between requests (configurable)
- Respectful to the server
- Prevents rate limiting issues

### Error Handling
- Comprehensive error reporting
- Continues processing even if some pages fail
- Detailed summary of successes and failures

## 📋 API Coverage

The scraper covers all RuneLite API classes and interfaces, including:

- **Core API**: Client, Player, NPC, GameObject, etc.
- **Events**: All event classes in `net.runelite.api.events`
- **Coordinates**: WorldPoint, LocalPoint, Angle, etc.
- **Widgets**: Widget, WidgetItem, etc.
- **Utilities**: Various utility classes and helpers

## 🤖 LLM Usage

The generated markdown files are optimized for LLM consumption:

- **Clean formatting** with proper headings and code blocks
- **Structured content** with consistent metadata
- **Complete coverage** of all RuneLite API functionality
- **Easy navigation** with table of contents and clear sections

## 🔧 Configuration

### Command Line Options
- `--test`: Run test with single URL only
- `--all`: Scrape all RuneLite API URLs (default)
- `--output DIR`: Output directory (default: scraped_docs)
- `--delay SECONDS`: Delay between requests (default: 1.0)

### Customization
You can modify `urls.py` to customize URL discovery or manually add URLs. The scraper behavior can be adjusted in `scraper.py`.

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Add new features

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**RuneLite API Documentation**: https://static.runelite.net/runelite-api/apidocs/  
**Branch**: runelite-docs-scraper
