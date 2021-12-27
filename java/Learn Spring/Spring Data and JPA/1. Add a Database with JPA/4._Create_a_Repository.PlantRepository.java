package com.codecademy.plants.repositories;

import org.springframework.data.repository.CrudRepository;
import com.codecademy.plants.entities.Plant;

public interface PlantRepository extends CrudRepository<Plant, Integer> {

}
