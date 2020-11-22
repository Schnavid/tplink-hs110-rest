# tplink-hs110-rest
Python3 based REST server for reading energy information from tplink hs110 smart plug. Should also work with the hs100 model.

## Dependencies
- pip3 install Flask

## Routes

### [GET] energy data

**Request**

http://127.0.0.1:1337/api/v1/energy?ip=192.168.1.29&port=9999

**Example Response**

```
{
    "emeter": {
        "get_realtime": {
            "voltage_mv": 231742,
            "current_ma": 143,
            "power_mw": 7448,
            "total_wh": 10701,
            "err_code": 0
        }
    }
}
```

### [GET] monthly stats

**Request**

http://127.0.0.1:1337/api/v1/monthly?ip=192.168.1.29&port=9999&year=2020

**Example Response**

```
{
    "emeter": {
        "get_monthstat": {
            "month_list": [
                {
                    "year": 2020,
                    "month": 10,
                    "energy_wh": 4354
                },
                {
                    "year": 2020,
                    "month": 11,
                    "energy_wh": 28652
                }
            ],
            "err_code": 0
        }
    }
}
```

## Notes

Currently there is no error handling implemented. But should not cause any problems if the correct ip and port of 
your smartplug is used.
