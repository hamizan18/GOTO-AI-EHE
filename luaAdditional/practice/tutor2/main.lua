function love.load()
    x = 100
    y = 250
    hp = 10
end

function love.update(dt)
    if love.keyboard.isDown("d") then
        x = x + 100 * dt
    end

    if love.keyboard.isDown("a") then
        x = x - 100 * dt
    end

    if love.keyboard.isDown("w") then
        y = y - 100 * dt
    end

    if love.keyboard.isDown("s") then
        y = y + 100 * dt
    end
end

function love.draw() 
    love.graphics.rectangle("fill", x, y, 40, 40)
    love.graphics.print("HP: " .. hp, 10, 10)
end