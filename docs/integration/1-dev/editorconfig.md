
## Workflow | Issue

- [ ] CONFIG: 
	- [ ] Repo | Agile | Plan | Design | Build | Integrate | Test | Quality |  Config | Deploy | Release
- [ ] GitHub Issue(s) Created?
	- [ ] FLOW: Workflow | Process | Outline
		- [ ] #Issue
	- [ ] LINT: Report
		- [ ] #Issue
- [x] FLOW
   - [x] Local Script
	   - [x] Bash?
   - [x] IDE Configuration
   - [ ] Pre-Commit
   - [ ] CI Workflow

# Package: 

**`Intent | Purpose:`**
```ruby
>> EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs.
>> The EditorConfig project consists of **a file format** for defining coding styles and a collection of **text editor plugins** that enable editors to read the file format and adhere to defined styles. 
>> EditorConfig files are easily readable and they work nicely with version control systems.
```

- SiteL [EditorConfig](https://editorconfig.org/)
- Related Config
	- [[CONFIG - {{}}]]
	- .

## Package | Library Source

- [ ] PIP
- [x] NPM
- [ ] Unpkg
- [ ] JsDeliver

**`ÙRL`**
```bash

```

### Source

- [EditorConfig Plugin](https://editorconfig.org/#download)
- [EditorConfig No PLugin](https://editorconfig.org/#pre-installed)

```bash

```

#### Dependencies

`None`
```bash

```

### Install

```bash
' locally'
npm install editorconfig
'globally'
npm install -g editorconfig
```

#### IDE

- [x] Pycharm
- [x] Webstorm
 
### Config

```json
"devDependencies": {  
	"editorconfig": "^2.0.0",    
},
```

```ini
# EditorConfig is awesome: https://EditorConfig.org  
# Code Insititute Code Style Basics  
  
# top-most EditorConfig file  
root = true  
  
# Unix-style newlines with a newline ending every file  
[*]  
indent_style = space # Python PEP8 Style Guide as dominant factor  
end_of_line = lf  
trim_trailing_whitespace = true # IDE | Pre-commit Linting  
insert_final_newline = true # IDE | Pre-commit Linting  
  
# Match Front-end Files with  
[*.{html,css,scss}]  
charset = utf-8 # IDE | Pre-commit Linting | File Compatibility  
indent_size = 4 # Consistency but individually controllable  
max_line_length = 120 #PyCharm, WebStorm  
  
# Matches multiple files with brace expansion notation  
# Set default charset  
[*.{js,py}]  
charset = utf-8 # IDE | Pre-commit Linting | File Compatibility  
  
# 4 space indentation  
[*.js]  
# indent_style = space  
indent_size = 4 # Consistency but individually controllable  
max_line_length = 100 #PyCharm, WebStorm  
  
[*.py]  
# indent_style = space  
indent_size = 4 # Python PEP8 Style Guide as dominant factor, indent size is critical for Python  
max_line_length = 80 # Autopep8 default #PyCharm, WebStorm  
  
# Matches the exact files either package.json or .travis.yml  
[{package.json,.travis.yml}]  
# indent_style = space  
indent_size = 2
```

#### ~~Requirements | Proc 

~~**PYTHON**: **`Requirements | Requirements-dev | Requirements-test`**~~
```text

```

```json

```

```yml

```


### Options | Usage

- Docs: [EditorConfig](https://editorconfig.org/)
- Package:
	- JS [editorconfig - npm (npmjs.com)](https://www.npmjs.com/package/editorconfig)
	- Py: [editorconfig/editorconfig-core-py: Clone of EditorConfig core written in Python (github.com)](https://github.com/editorconfig/editorconfig-core-py)
- GitHub:
- Perplexity:

```json
{
  config: '.editorconfig',
  version: pkg.version,
  root: '/',
  files: undefined,
  cache: undefined,
  unset: false,
};
```

## Final
> FLOW

### Steps

1. Define the .editorconfig file.
2. Configure the IDE for actions on save etc
3. Decide to use a pre-commit.
4. Commit to repository.

### Repository

```dirtree

- /dash-and-do-github
	- /.github
		- /workflows
			- .yml
	- /docs
		- /integration
			- /1-dev
				- file.md
	- /scripts
		- /1-dev
			- .sh
	- .file
```



