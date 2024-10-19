# Oura Targeted Data Extraction

This Python script facilitates the extraction of various data types from the Oura API, including sleep, activity, heart rate, personal information, and more. It allows users to retrieve specific data within a defined date range and store the results in a local directory.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Data Retrieval](#data-retrieval)
- [Contributing](#contributing)
- [License](#license)

## Features

- Extracts different types of user data from the Oura API, including:
  - Daily Activity
  - Daily Heart Rate
  - Sleep Data
  - Personal Information
  - Readiness and Rest Mode Data
  - Workout and Tag Data
  - Ring Configuration
- Saves the data in JSON format within a newly created folder named after the current date.

## Requirements

- Python 3.x
- Python libraries:
  - `requests`
  - `os`
  - `json`
  - `datetime`
- Oura API Token (to be set within the script)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/oura-targeted-extraction.git
   cd oura-targeted-extraction
   ```

2. Add your Oura API token:
   - Replace `'YOUR_API_TOKEN_HERE'` in the script with your valid Oura API token.

## Usage

Run the script from the command line by specifying the start and end dates in the format `YYYY-MM-DD`:

```bash
python oura_targeted_extraction.py <start_date> <end_date>
```

Example:
```bash
python oura_targeted_extraction.py 2023-10-01 2023-10-10
```

The extracted data will be saved in a folder named with the current date in the working directory.

## Data Retrieval

The script retrieves the following data from the Oura API:
- **Daily Activity:** Provides the user's activity metrics.
- **Heart Rate:** Extracts the user's daily heart rate data.
- **Personal Information:** Fetches user profile information.
- **Sleep Data:** Retrieves data related to sleep, including timing and stages.
- **Readiness:** Captures data related to the user's readiness scores.
- **Rest Mode:** Fetches rest mode status.
- **Workouts:** Provides information about recorded workouts.
- **Tags:** Retrieves user-defined tags.
- **Ring Configuration:** Captures the configuration details of the user's Oura Ring.

The data is saved in JSON files within a directory named as `<current_date>_data`.

## Contributing

Contributions to enhance the functionality of this script are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```
