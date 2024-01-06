<a  href="https://www.buymeacoffee.com/ajayagrawal">![ClutterCureHeader](https://github.com/ajayagrawalgit/ClutterCure/assets/94609372/4042cab2-6bbd-44fb-b92d-5099c53bd89d) </a>
<p align="center">
<a href="https://github.com/ajayagrawalgit/ClutterCure/blob/main/LICENSE" title="License">
<img src="https://img.shields.io/github/license/ajayagrawalgit/ClutterCure?label=License&logo=Github&style=flat-square" alt="ClutterCure License"/>
</a>
<a href="https://github.com/ajayagrawalgit/ClutterCure/fork" title="Forks">
<img src="https://img.shields.io/github/forks/ajayagrawalgit/ClutterCure?label=Forks&logo=Github&style=flat-square" alt="ScareCrypt Forks"/>
</a>
<a href="https://github.com/ajayagrawalgit/ClutterCure/stargazers" title="Stars">
<img src="https://img.shields.io/github/stars/ajayagrawalgit/ClutterCure?label=Stars&logo=Github&style=flat-square" alt="ScareCrypt Stars"/>
</a>
<a href="https://github.com/ajayagrawalgit/ClutterCure/issues" title="Issues">
<img src="https://img.shields.io/github/issues/ajayagrawalgit/ClutterCure?label=Issues&logo=Github&style=flat-square" alt="ScareCrypt Issues"/>
</a>
<a href="https://github.com/ajayagrawalgit/ClutterCure/pulls" title="Pull Requests">
<img src="https://img.shields.io/github/issues-pr/ajayagrawalgit/ClutterCure?label=Pull%20Requests&logo=Github&style=flat-square" alt="ScareCrypt Pull Requests"/>
</a>
<a href="https://github.com/ajayagrawalgit/ClutterCure" title="Repo Size">
<img src="https://img.shields.io/github/repo-size/ajayagrawalgit/ClutterCure?label=Repo%20Size&logo=Github&style=flat-square" alt="ScareCrypt Repo Size"/>
</a>

ClutterCure is a Platform Independent Utility made with Python designed to help you organize and declutter your files by categorizing them into directories based on their file types. It comes with logging functionality to keep track of the organization process.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Use Cases](#use-cases)
- [Configuration](#configuration)
- [Supported File Types](#supported-file-types)
- [Contributing](#contributing)
- [License](#license)

<br>

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ajayagrawalgit/ClutterCure.git
   cd ClutterCure
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

<br>

## Configuration

Modify the `config.yaml` file under `./src` directory to customize the behavior of ClutterCure. The configuration file includes various settings:

- `path_to_organise`: The path to the directory you want to organize.
- `time_zone`: Time zone for logging purposes (e.g., "America/New_York"). See `help/supported_time_zones.txt` to see the list of supported time zones.
- `logs`: Paths for the main and error log files.
- `file_types`: Supported file types and their corresponding extensions.

Example `config.yaml`:

```yaml
# Configuration file for ClutterCure

version: 1.0

path_to_organise: "/path/to/your/directory"
time_zone: "Your/Time_Zone"
logs:
  error_log: "/path/to/error/log/file.log"
  main_log: "/path/to/main/log/file.log"
file_types:
  Images: ['img', 'jpeg', 'gif', 'jpg', 'bmp', 'png']
  PDFs: ['pdf']
  Docs: ['doc', 'docx']
  # Add more file types as needed
```


## Supported File Types

ClutterCure allows you to organize files into directories based on their types, providing flexibility and customization. The supported file types and their corresponding extensions are configured in the `config.yaml` file. Adjust the file types according to your specific needs and preferences.

```yaml
file_types:
  Images: ['img', 'jpeg', 'gif', 'jpg', 'bmp', 'png']
  PDFs: ['pdf']
  Docs: ['doc', 'docx']
  # Add or modify file types as needed
```

**Note:** Folders corresponding to the defined file types will be automatically created within the `path_to_organise` directory. In the example above, folders named `Images`, `PDFs`, and `Docs` will be generated under `/path/to/your/directory` if they do not already exist.

<br>

## Usage

Run the `cluttercure.py` script to organize the files in the specified directory:

```bash
python cluttercure.py
```

Make sure to configure the `config.yaml` file correctly before running the script.

<br>



## Use Cases

### 1. Scheduled File Organization

**Scenario:** ClutterCure can be configured as a scheduled task or cron job, allowing you to automate the organization of files in a specific directory at regular intervals.

**Benefit:** Ensures continuous and systematic file organization without requiring manual intervention. Ideal for maintaining a well-ordered file system.

---

### 2. Post-Download File Sorting

**Scenario:** By integrating ClutterCure with a download directory, you can automate the sorting of downloaded files into categorized folders based on their types.

**Benefit:** Keeps your download directory neat and well-organized, making it easier to locate and manage downloaded files. Streamlines post-download file handling.

---

### 3. Project-Specific File Structuring

**Scenario:** ClutterCure can be employed within a project to automatically structure and categorize project-related files based on their types.

**Benefit:** Maintains a clean and organized project directory structure, enhancing collaboration and making it easier for team members to find relevant files throughout the project's lifecycle.

---

### 4. Automated Backup Organization

**Scenario:** Utilize ClutterCure to organize backup files systematically by their types, simplifying the process of locating specific backups when needed.

**Benefit:** Facilitates efficient backup management by structuring backup files based on their formats. This makes it quicker and easier to identify and restore specific backups.

---

### 5. Cloud Storage Cleanup

**Scenario:** Apply ClutterCure to automatically organize files within a cloud storage directory, ensuring a well-structured storage system.

**Benefit:** Enhances the accessibility and retrieval of files within cloud storage by maintaining a structured organization. This helps optimize storage space and streamlines file management in cloud-based environments.

These use cases illustrate how ClutterCure can be seamlessly integrated into various scenarios to automate file organization, thereby improving overall file management processes in different contexts.


<br>


## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request.

1. **Fork the repository.**
2. **Create your feature branch:**
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Commit your changes:**
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/new-feature
   ```
5. **Open a pull request.**

<br>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


<br>
<br>

 ## 🧑🏻 Know Me More
Developer - <b> Ajay Agrawal </b>
<br>
- 🌌 [Profile](https://github.com/ajayagrawalgit "Ajay Agrawal")
- 🏮 [Email](mailto:ajayagrawalhere@gmail.com?subject=Hi%20from%20<repo-email> "Hi!")

<br>
<br>
<h2 align="center"> 🤝 Support Me 🤝 <h2>
<p align="center">
<a href="https://www.buymeacoffee.com/ajayagrawal" title="Buy me a Coffee"><img src="https://user-images.githubusercontent.com/94609372/232127833-d03502af-baf2-46e3-a045-0f7c84531a61.png" alt="Buy me a Coffee"/></a>
</p>
<br><br>
<h4>
<br>
<p align="center"> Made with ♥️ in India </p>
<br>
