t = 0

function love.update(dt)
    t = t + dt
end

function love.draw()
    local x = 400 + math.cos(t) * 100
    local y = 300 + math.sin(t) * 100
    love.graphics.circle("fill", x, y, 25)
end