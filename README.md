# dnspapin
                                                      
                ooo.   o    o .oPYo.    .oPYo.                o       
                8  `8. 8b   8 8         8    8                        
                8   `8 8`b  8 `Yooo.   o8YooP' .oPYo. .oPYo. o8 odYo. 
                8    8 8 `b 8     `8    8      .oooo8 8    8  8 8' `8 
                8   .P 8  `b8      8    8      8    8 8    8  8 8   8 
                8ooo'  8   `8 `YooP'    8      `YooP8 8YooP'  8 8   8 
                .....::..:::..:.....::::..::::::.....:8 ....::....::..
                ::::::::::::::::::::::::::::::::::::::8 ::::::::::::::



                .-----.                                _.----"""""""----._
          _.---//-"""-\\---._            .------.___  (                   )
         (   (/        `-'   )          (        ___|-|`"""---..___..---""|
        _|`"--._________.--"'|_          `---'"""     |                   |
       (_|                   |_)                      |                   |
       `--)                 (--'          ________    |                   |
         |                   |   _.--"""""        """"----._              |
         |                   |  (_                         _)--.----------------.
         |                   |   \`""---...________...----'/__/___             ||
         `-.__           __.-'    \___                  __/ ""-----"""""""-----`'
              `""-----""'              ""`-----------'""


Want to cook up some tasty DNS packets?
DNS Papin is a DNS traffic generation tool designed to help you simulate DNS traffic for testing purposes. By generating DNS queries according to your specifications, DNS Papin enables you to evaluate the performance of your DNS infrastructure.

### Installation
- Clone the DNS Papin repository to your local machine
- Install poetry in your virtual environment using `pip install poetry`
- Run `poetry install`

You can now run DNS Papin with `poetry run python dns_papin --config config.yml`

### Example configuration
DNS Papin can be configured via a YAML file or by using environment variables with the same name, prefixed with `PAPIN_`.

```yaml
target: "localhost"
port: 53
file: "examples.txt"
delimiter: ","
thread_count: 100
```

In this configuration:

- `target` specifies the DNS server to query
- `port` specifies the destination port
- `file` specifies the file containing DNS queries to send
- `delimiter` specifies the delimiter used to separate domain names and record types in the query file
- `thread_count` specifies the number of threads to use for concurrent DNS query generation

DNS Papin will continuously cycle through the records listed in the `examples.txt` file.

```
google.com,A
volny.cz,AAAA
```