
def count_batteries_by_health(present_capacities):
  values={
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for capacity in present_capacities:
    
      SoH=100 * capacity /120

      if SoH>80:
        values["healthy"]+=1
        
      elif 65 <=SoH <=80:
        values["exchange"]+=1
      else:
        values["failed"]+=1
      
  return values
  


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  for k,i in counts.items():
    print(f"{k} {i}")
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
