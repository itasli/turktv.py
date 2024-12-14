import functools
from typing import Dict, Any, Callable, Optional

class ChannelRegistry:
    """
    Centralized manager for registering and managing channels
    """
    _channels: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def _normalize_key(cls, name: str) -> str:
        """
        Normalize the channel name to create a unique key
        
        :param name: Channel name
        :return: Normalized key
        """
        return name.lower().replace(' ', '_')

    @classmethod
    def update_resolvers(cls, router):
        """
        Dynamically updates the resolver URLs in the registry based on the router routes.
        
        :param router: The FastAPI router
        """
        for route in router.routes:
            # check if route name is not None, and if it is a registered channel
            if route.name and cls._normalize_key(route.name) in cls._channels:
                # Update the resolver URL
                cls._channels[cls._normalize_key(route.name)]['resolver'] = route.path

    @classmethod
    def register_channel(cls, name: str, logo: Optional[str] = None, order: float = 0.0):
        """
        Decorator to automatically register a channel
        
        :param name: Channel name
        :param logo: Logo URL (optional)
        :param order: Order of the channel (optional)
        :return: Decorator
        """
        def decorator(func: Callable):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            # Unique key based on the name (normalized)
            key = cls._normalize_key(name)
            
            # Registering channel metadata
            cls._channels[key] = {
                'name': name,
                'logo': logo,
                'order': order,
            }
            
            return wrapper
        return decorator

    @classmethod
    def get_channels(cls, sort_by_order: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Retrieves all registered channels
        
        :param sort_by_order: Sort channels by their order (optional)
        :return: Dictionary of channels with resolved URLs
        """
        if sort_by_order:
            return dict(sorted(cls._channels.items(), key=lambda x: x[1]['order']))
        return cls._channels.copy()


    @classmethod
    def get_channel(cls, channel_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a specific channel
        
        :param channel_name: Channel name
        :return: Channel information or None
        """
        return cls._channels.get(cls._normalize_key(channel_name))
