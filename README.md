# DomainAvailabilityChecker

This script is used to determine the availability of domain names given a list of words and domain name extensions chosen by the user


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```python
pip install -r requirements.txt
```

## Usage
1. Place all the domain names (excluding extensions) in the ```words.txt``` file. Here's an example:
    ```bash
    apple
    orange
    peach
    ```
2. Add domain extensions of interest to the ```DOMAIN_EXTENSIONS``` list in ```config.py```

3. Run script
    * starting at first word in ```words.txt``` :
        ```bash
        python domain_availability_checker/main.py 
        ```
    * starting at Nth word in ```words.txt```:
        ```bash
        python domain_availability_checker/main.py --start_index {integer}
        ```
4. Output is a JSON file:        
   ```bash
    available_domains.json
   ```
## Additional Information
This script can check 600 domain names per hour due to the request limit on whois servers

Please see the ```whois``` [github page](https://github.com/DannyCork/python-whois) for more information regarding supported domain name extensions.


## License
[MIT](https://choosealicense.com/licenses/mit/)