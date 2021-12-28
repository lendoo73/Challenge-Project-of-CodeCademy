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

  @GetMapping("/plants/search")
  public List<Plant> searchPlants(
    @RequestParam(name="hasFruit", required = false) Boolean hasFruit,
    @RequestParam(name="maxQuantity", required = false) Integer quantity
  ) {
    if (hasFruit != null && quantity != null && hasFruit) {
      return this.plantRepository.findByHasFruitTrueAndQuantityLessThan(quantity);
    }
    if (hasFruit != null && quantity != null && !hasFruit) {
      return this.plantRepository.findByHasFruitFalseAndQuantityLessThan(quantity);
    }
    if (hasFruit != null && hasFruit) {
      return this.plantRepository.findByHasFruitTrue();
    }
    if (hasFruit != null && !hasFruit) {
      return this.plantRepository.findByHasFruitFalse();
    }
    if (quantity != null) {
      return this.plantRepository.findByQuantityLessThan(quantity);
    }
    return new ArrayList<>();
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

  @PutMapping("/plants/{id}")
  public Plant updatePlant(@PathVariable("id") Integer id, @RequestBody Plant p) {
    Optional<Plant> plantToUpdateOptional = this.plantRepository.findById(id);
    if (!plantToUpdateOptional.isPresent()) {
      return null;
    }
    Plant plantToUpdate = plantToUpdateOptional.get();
    if (p.getHasFruit() != null) {
      plantToUpdate.setHasFruit(p.getHasFruit());
    }
    if (p.getQuantity() != null) {
      plantToUpdate.setQuantity(p.getQuantity());
    }
    if (p.getName() != null) {
      plantToUpdate.setName(p.getName());
    }
    if (p.getWateringFrequency() != null) {
      plantToUpdate.setWateringFrequency(p.getWateringFrequency());
    }
    Plant updatedPlant = this.plantRepository.save(plantToUpdate);
    return updatedPlant;
  }

  @DeleteMapping("/plants/{id}")
  public Plant deletePlant(@PathVariable("id") Integer id) {
    Optional<Plant> plantToDeleteOptional = this.plantRepository.findById(id);
    if (!plantToDeleteOptional.isPresent()) {
      return null;
    }
    Plant plantToDelete = plantToDeleteOptional.get();
    this.plantRepository.delete(plantToDelete);
    return plantToDelete;
  }

}
