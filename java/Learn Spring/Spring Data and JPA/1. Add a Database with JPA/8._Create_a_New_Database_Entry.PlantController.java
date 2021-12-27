package com.codecademy.plants.controllers;

import java.lang.Iterable;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

import com.codecademy.plants.entities.Plant;
import com.codecademy.plants.repositories.PlantRepository;

@RestController
public class PlantController {

  private final PlantRepository plantRepository;

  public PlantController(final PlantRepository plantRepository) {
    this.plantRepository = plantRepository;
  }

  @GetMapping("/plants")
  public Iterable<Plant> getAllPlants() {
    return this.plantRepository.findAll();
  }

  @GetMapping("/plants/{id}")
  public Optional<Plant> getPlantById(@PathVariable("id") Integer id) {
    return this.plantRepository.findById(id);
  }

  @PostMapping("/plants")
  public Plant createNewPlant(@RequestBody Plant plant) {
    Plant newPlant = this.plantRepository.save(plant);
    return newPlant;
  }

}
