package com.codecademy.plants.controllers;

import com.codecademy.plants.repositories.PlantRepository;

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


@RestController
public class PlantController {
  private final PlantRepository plantRepository;

  public PlantController(PlantRepository plantRepository) {
    this.plantRepository = plantRepository;
  }
}
