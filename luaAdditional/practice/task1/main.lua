function love.load()
    hp = 100
    x = 200
    y = 200
    speed = 100
end

function love.update(dt)
    if love.keyboard.isDown("a") then
        x = x - speed * dt
    end
    if love.keyboard.isDown("d") then
        x = x + speed * dt
    end
    if love.keyboard.isDown("w") then
        y = y - speed * dt
    end
    if love.keyboard.isDown("s") then
        y = y + speed * dt 
    end
    if love.keyboard.isDown("space") then
        hp = hp - 10
    end
end

function love.draw() 
    love.graphics.rectangle("fill", x, y, 40, 40)
    love.graphics.rectangle("fill", x, (y + 2), (hp / 10), 5)
end