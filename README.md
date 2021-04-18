# Run in dev
Source the venv and start the backend

`$ source venv/bin/activate`


`$ ./runFastApi.sh`

## Troubleshooting

### Check the current installed pip packages first:
`$ pip freeze`
### If pip is not installed:
`$ pacman -S python-pip`

### If pip freeze is not the same as requirements.txt:
Stop and remove the current venv

`$ deactivate`

`$ rm -rf venv`

Make a new venv and source it

`$ python -m venv venv`

`$ source venv/bin/activate`

Install the right requirements

`$ pip install -r requirements.txt`

