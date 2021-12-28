package com.codecademy.boots.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.codecademy.boots.entities.Boot;
import com.codecademy.boots.enums.BootType;

public interface BootRepository extends CrudRepository<Boot, Integer> {
  List<Boot> findBySize(Float size);
  List<Boot> findByMaterial(String material);
  List<Boot> findByType(BootType type);
  List<Boot> findByQuantityGreaterThanEqual(Integer quantity);
  
  // material, type, size, and minimum quantity
  List<Boot> findByMaterialAndTypeSizeAndQuantityGreaterThanEqual(String material, BootType type, Float size, Integer quantity);

  // material, size, and type
  List<Boot> findByMaterialAndSizeAndType(String material, Float size, BootType type);

  // material, a type, and a minimum quantity
  List<Boot> findByMaterialAndTypeAndQuantityGreaterThanEqual(String material, BootType type, Integer quantity);

  // material and a type
  List<Boot> findByMaterialAndType(String material, BootType type);

  // type, size, and minimum quantity
  List<Boot> findByTypeAndSizeAndQuantityGreaterThanEqual(BootType type, Float size, Integer quantity);

  // type and a size
  List<Boot> findByTypeAndSize(BootType type, Float size);

  // type and a minimum quantity
  List<Boot> findByTypeAndQuantityGreaterThanEqual(BootType type, Integer quantity);

  // size and a minimum quantity
  List<Boot> findBySizeAndQuantityGreaterThanEqual(Float size, Integer quantity);


}

