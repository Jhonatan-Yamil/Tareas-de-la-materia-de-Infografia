extends CharacterBody2D

@export var target: Node2D = null
@export var max_speed = 50
@onready var navigation: NavigationAgent2D = $NavigationAgent2D
@onready var chicken_scene = preload("res://scenes/chicken.tscn")

var current_egg: Node2D = null

func setup():
	await get_tree().physics_frame
	if target:
		navigation.target_position = target.global_position

func _ready() -> void:
	call_deferred("setup")
	print(navigation.get_current_navigation_path())
	$CollisionShape.connect("body_entered", Callable(self, "_on_collision_shape_body_entered"))

func _physics_process(delta: float) -> void:
	var eggs = get_tree().get_nodes_in_group("Egg")
	if eggs.size() > 0:
		var closest_egg = find_closest_egg(eggs)
		if closest_egg != current_egg:
			current_egg = closest_egg
			navigation.target_position = current_egg.global_position
	
	if navigation.is_navigation_finished():
		return
	
	var next_path_position = navigation.get_next_path_position()
	velocity = global_position.direction_to(next_path_position) * max_speed
	move_and_slide()

func find_closest_egg(eggs: Array) -> Node2D:
	var closest_egg = eggs[0]
	var closest_distance = global_position.distance_to(eggs[0].global_position)
	
	for egg in eggs:
		var distance = global_position.distance_to(egg.global_position)
		if distance < closest_distance:
			closest_egg = egg
			closest_distance = distance
	
	return closest_egg

func _on_collision_shape_body_entered(body: Node2D) -> void:
	if body.is_in_group("Egg"):
		call_deferred("_spawn_chicken", body.global_position)
		body.queue_free()
		current_egg = null

func _spawn_chicken(position: Vector2):
	var new_chicken = chicken_scene.instantiate()
	new_chicken.global_position = position
	get_parent().add_child(new_chicken)
