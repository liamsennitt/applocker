# AppLocker

[![GitHub Workflow Status (branch)](https://img.shields.io/github/actions/workflow/status/liamsennitt/applocker/build.yml?branch=main)](https://github.com/liamsennitt/applocker/actions/workflows/build.yml)
[![PyPI](https://img.shields.io/pypi/v/applocker)](https://pypi.org/project/applocker/)
[![GitHub](https://img.shields.io/github/license/LiamSennitt/applocker)](LICENSE)

The `applocker` module allows you to easily parse and create Windows AppLocker Policy XML files and/or strings in Python.

## Installation

To install the `applocker` module via pip, run the command:

```console
$ pip install applocker
```

## Usage

Start by importing the `applocker` module.

```python
import applocker
```

The function `applocker.load`, loads an AppLocker Policy XML file.

```python
with open('example.xml', 'r') as file:
    applocker.load(file)
```

The function `applocker.loads`, loads an AppLocker Policy XML string.

```python
applocker.loads('<AppLockerPolicy Version="1" />')
```

In addition to loading an existing AppLocker Policy, policies created using the relevant Conditions, Rules and Rule Collections can be dumped to an XML file using the `applocker.dump` function.

```python
with open('example.xml', 'w') as file:
    applocker.dump(policy, file)
```

Or, an XML string using the `applocker.dumps` function.

```python
applocker.dumps(policy)
```

### FilePublisherRule

To create a file publisher AppLocker rule to allow or deny digitally signed files, a `applocker.conditions.FilePublisherCondition` must be created optionally specifying a `applocker.conditions.BinaryVersionRange`.

This condition can then be used to create a `applocker.rules.FilePublisherRule`.

```python
from applocker.conditions import BinaryVersionRange, FilePublisherCondition
from applocker.rules import FilePublisherRule

binary_version_range = BinaryVersionRange(low_section='10.0.19041.1', high_section='10.0.19041.1')

condition = FilePublisherCondition(
    publisher_name='O=MICROSOFT CORPORATION, L=REDMOND, S=WASHINGTON, C=US',
    product_name='MICROSOFT® WINDOWS® OPERATING SYSTEM',
    binary_name='CMD.EXE',
    binary_version_range=binary_version_range
)

rule = FilePublisherRule(
    id='00000000-0000-0000-0000-000000000000',
    name='Deny everyone execution of cmd.exe',
    description='',
    user_or_group_sid='S-1-1-0',
    action='Deny',
    conditions=[
        condition
    ]
)
```

### FilePathRule

To create a file path AppLocker rule to allow or deny files based upon their path, a `applocker.conditions.FilePathCondition` condition must be created.

This condition can then be used to create a `applocker.rules.FilePathRule`.

```python
from applocker.conditions import FilePathCondition
from applocker.rules import FilePathRule

condition = FilePathCondition(path='C:\Windows\System32\cmd.exe')

rule = FilePathRule(
    id='00000000-0000-0000-0000-000000000000',
    name='Deny everyone execution of cmd.exe',
    description='',
    user_or_group_sid='S-1-1-0',
    action='Deny',
    conditions=[
        condition
    ]
)
```

### FileHashRule

To create a file hash AppLocker rule to allow or deny files based upon their hash, one or more `applocker.conditions.FileHash` objects and a `applocker.conditions.FileHashCondition` condition must be created.

This condition can then be used to create a `applocker.rules.FileHashRule`.

```python
from applocker.conditions import FileHash, FileHashCondition
from applocker.rules import FileHashRule

hash = FileHash(
    type='SHA256',
    data='0x9BB897814C6E1A2A2701D2ADB59AAC2BCACB9CF265DDF3F61B9056EA6FFE04C7',
    source_file_name='cmd.exe',
    source_file_length='289792'
)

condition = FileHashCondition(file_hashes=[hash])

rule = FileHashRule(
    id='00000000-0000-0000-0000-000000000000',
    name='Deny everyone execution of cmd.exe',
    description='',
    user_or_group_sid='S-1-1-0',
    action='Deny',
    conditions=[
        condition
    ]
)
```

### RuleCollection

To create a rule collection one or more rules must be created as described above.

These rules can then be used to create a `applocker.rules.RuleCollection`.

```python
from applocker.rules import RuleCollection

rule_collection = RuleCollection(
    type='Exe',
    enforcement_mode='Enforcing',
    rules=[
        rule
    ]
)
```

### AppLockerPolicy

To create an AppLocker Policy one or more rule collections must be created as described above.

These rule collections can then be used to create an `applocker.policy.AppLockerPolicy`.

```python
from applocker.policy import AppLockerPolicy

policy = AppLockerPolicy(
    version='1',
    rule_collections=[
        rule_collection
    ]
)
```
