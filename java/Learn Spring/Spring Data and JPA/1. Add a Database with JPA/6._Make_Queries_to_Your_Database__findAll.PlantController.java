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

import com.codecademy.plants.repositories.PlantRepository;
import com.codecademy.plants.entities.Plant;

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

}
