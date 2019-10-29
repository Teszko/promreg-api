# promregapi Python client

a Python client to easily query, register and delete targets with Prometheus Registration.

## Usage

#### Initialization
````python
from promregapi import PromRegApi

hostname = "hostname of your Prometheus Registration Server"
api_token = "secret"

promreg = PromRegApi(hostname, api_token)
````
#### PromRegApi optional parameters
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `protocol` | `string` | http or https (default http) |
| `port` | `int` | (default 12321) |
| `basepath` | `string` | uri prefix for targets. (default targets/) |
| `comment` | `string` | comment (default "added by promregapi") |

   

#### Get registered targets
````python
promreg.get(uri="")
````
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `uri` | `string` | hostname or ip and port of target. Returns all targets if called without parameter |
   

#### register target
````python
promreg.register(target, comment=None, labels=None)
````
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `target` | `string` | the hostname or ip and port of target |
| `comment` | `string` | comment describing this target |
| `labels` | `object` | prometheus labels |
   
   
#### delete registered target
````python
promreg.delete(target)
````
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `target` | `string` | the hostname or ip and port of target |
   

#### update registered target
````python
promreg.update(target, comment=None, labels=None)
````
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `target` | `string` | the hostname or ip and port of target |
| `comment` | `string` | comment describing this target |
| `labels` | `object` | prometheus labels |
