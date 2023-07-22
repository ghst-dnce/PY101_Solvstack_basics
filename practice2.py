is_raining = False
is_freezing = False
is_night_time = False
is_dog_outside = False

if is_dog_outside:
  if is_raining or is_freezing or is_night_time:
    print("Bring your dog inside!")
  else:
    print("Fido can continue enjoying the great outdoors!")
else:
  print("Your dog wants to go outside!")