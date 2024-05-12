agencies = {
    "CBI" : "Central Bureau of Investigation",
    "FBI" : "Foreign Direct Investment",
    "NIA" : "National Investion Agency",
    "SSB" : "Service Selection Board",
    "WPA" : "Works Progress Administration" 
}
print("\nagencies: \n", agencies)
print("\nType of Agencies : ", type(agencies))

# a.
agencies["BSE"] = "Bombay Stock Exchange"
print("\nagencies after adding BSE: \n", agencies)

# b.
agencies.update({"SSB" : "Social Security Administration" })
print("\n\nagencies after changing SSB: \n", agencies)

# c.
agencies.pop("CBI")
agencies.pop("WPA")
print("\n\nagencies after deleting CBI and WPA: \n", agencies)

