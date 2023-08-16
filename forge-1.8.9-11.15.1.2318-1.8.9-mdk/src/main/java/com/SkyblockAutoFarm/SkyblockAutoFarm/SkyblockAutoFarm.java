package com.SkyblockAutoFarm.SkyblockAutoFarm;

import net.minecraft.block.state.IBlockState;
import net.minecraft.init.Blocks;
import net.minecraft.init.Items;
import net.minecraft.item.ItemStack;
import net.minecraft.world.World;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.entity.player.PlayerInteractEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;

@Mod(modid = SkyblockAutoFarm.MODID, version = SkyblockAutoFarm.VERSION)
public class SkyblockAutoFarm {
    public static final String MODID = "SkyblockAutoFarm";
    public static final String VERSION = "1.0";

    @EventHandler
    public void init(FMLInitializationEvent event) {
        MinecraftForge.EVENT_BUS.register(this);
    }

    @SubscribeEvent
    public void onPlayerInteract(PlayerInteractEvent event) {
        if (event.entityPlayer != null && event.pos != null) {
            ItemStack heldItem = event.entityPlayer.getHeldItem();

            if (heldItem != null
                    && (heldItem.getItem() == Items.diamond_axe || heldItem.getItem() == Items.golden_axe ||
                            heldItem.getItem() == Items.iron_axe || heldItem.getItem() == Items.stone_axe ||
                            heldItem.getItem() == Items.wooden_axe)) {
                World world = event.entityPlayer.worldObj;
                IBlockState state = world.getBlockState(event.pos);

                if (state.getBlock() == Blocks.log || state.getBlock() == Blocks.log2) {
                    world.destroyBlock(event.pos, true);
                }
            }
        }
    }
}
