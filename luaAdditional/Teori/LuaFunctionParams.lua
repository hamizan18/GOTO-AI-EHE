hp = 200

function takeDamage(damage) 
    hp = hp - damage
    if hp < 0 then hp = 0 end
    print("Your HP: " .. hp)
end

takeDamage(1000)