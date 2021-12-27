package com.codecademy.plants.entities;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.Column;
import javax.persistence.Id;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
@Table(name = "PLANTS")
public class Plant {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Integer id;

  @Column(name = "NAME")
  private String name;

  @Column(name = "QUANTITY")
  private Integer quantity;

  @Column(name = "WATERING_FREQUENCY")
  private Integer wateringFrequency;

  @Column(name = "HAS_FRUIT")
  private Boolean hasFruit;

  public Integer getId() {
    return this.id;
  }

  public String getName() {
    return this.name;
  }

  public Integer getQuantity() {
    return this.quantity;
  }

  public Integer getWateringFrequency() {
    return this.wateringFrequency;
  }

  public Boolean getHasFruit() {
    return this.hasFruit;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }

  public void setWateringFrequency(Integer wateringFrequency) {
    this.wateringFrequency = wateringFrequency;
  }

  public void setHasFruit(Boolean hasFruit) {
    this.hasFruit = hasFruit;
  }

}
