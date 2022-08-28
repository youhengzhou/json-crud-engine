# JSON Engine

please refer to https://pypi.org/project/jsonengine/ for the python package

and please refer to https://github.com/youhengzhou/json-crud-engine for the repo

# Download Package

`py -m pip install jsonengine -U`

## In Your Python Files

`import jsonengine`

# Commands

## Create command:

`eng.create(dictionary, path)`
This will create a JSON dictionary in the path

## Retrieve command:

`eng.retrieve(path)`
This will retrieve the JSON dictionary in the path

## Update command:

`eng.update(dictionary, path)`
This will update a JSON dictionary in the path

Update in this case means replacing the dictionary in its entirety with a new one

## Update (with key value) command:

`eng.update_kv(key, value, path)`
This will update a key value pair in the JSON dictionary in the path

Update in this case means replacing the dictionary with the key value pair

## Patch command:

`eng.patch(dictionary, path)`
This will patch a JSON dictionary in the path

Patch in this case means keeping the JSON dictionary in the path and appending to the dictionary

## Patch (with key value) command:

`eng.patch_kv(dictionary, path)`
This will patch a key value pair in the JSON dictionary in the path

Patch in this case means keeping the dictionary and appending the new key value pair

## Delete command:

`eng.delete(path)`

This will delete the JSON dictionary in the path
