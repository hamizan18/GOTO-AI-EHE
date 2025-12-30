function love.load()
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
end

function love.draw() 
    love.graphics.rectangle("fill", x, y, 40, 40)
end